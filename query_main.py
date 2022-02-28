# encoding=utf-8

"""
@desc:main函数，整合整个处理流程。
"""
#from settings import fuseki,q2s

STATIC_URL = '/static/'


import jena_sparql_endpoint
import question2sparql
# TODO 连接Fuseki服务器。
fuseki = jena_sparql_endpoint.JenaFuseki()
# TODO 初始化自然语言到SPARQL查询的模块，参数是外部词典列表。
q2s = question2sparql.Question2Sparql(['./dict/disease_pos.txt',
                                       './dict/medicine_pos.txt',
                                       './dict/symptom_pos.txt',
                                       './dict/therapy_pos.txt',
                                       './dict/examination_pos.txt'])
def query_function(question):
        while True:
            question = question
            #print(question.encode('utf-8'))
            #isinstance(question.encode('utf-8'))
            my_query = q2s.get_sparql(question.encode('utf-8'))
            #print(my_query)
            if my_query is not None:
                result = fuseki.get_sparql_result(my_query)
                value = fuseki.get_sparql_result_value(result)

                # TODO 查询结果为空，根据OWA，回答“不知道”
                if len(value) == 0:
                    return '知识库中并没有该问题的答案'
                elif len(value) == 1:
                    print(len(value[0]))
                    if len(value[0]) != 1:
                        return value[0]
                    else:
                        return value[0]
                else:
                    output = ''
                    for v in value:
                        output += v + u'、'
                    return output

            else:
                # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
                return '无法理解你的问题'

            #print('#' * 100)

def run(question):
    while True:
        my_query = q2s.get_sparql(question.encode('utf-8'))
        if my_query is not None:
            result = fuseki.get_sparql_result(my_query)
            value = fuseki.get_sparql_result_value(result)
            # TODO 判断结果是否是布尔值，是布尔值则提问类型是"ASK"，回答“是”或者“不知道”。
            if isinstance(value, bool):
                if value is True:
                    return "是的"
                else:
                    return "暂时还不知道呢"
            else:
                # TODO 查询结果为空，根据OWA，回答“不知道”
                if len(value) == 0:
                    return "暂时还不知道呢"
                # elif len(value) == 1:
                #     print(len(value[0]))
                #     print(value[0])
                else:  # TODO 能查到，输出查询结果
                    #return fuseki.print_result_to_string(result)
                    return value
                break

        else:
            # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
            return "暂时无法理解呢"

if __name__ == '__main__':
        #question = input('请输入你的问题：')
        question="膀胱癌概述"
        # question="膀胱癌的分期是怎样的？"
        # question="膀胱癌的治疗是怎样的？"
        value=run(question)
        print(value)


