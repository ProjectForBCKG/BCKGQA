# encoding=utf-8

"""
@desc: 将自然语言转为SPARQL查询语句
"""

import QTemplate
import word_tagging

class Question2Sparql:
    def __init__(self, dict_paths):
        self.tw = word_tagging.Tagger(dict_paths)
        self.rules = QTemplate.rules

    def get_sparql(self, question):
        """
        进行语义解析，找到匹配的模板，返回对应的SPARQL查询语句
        :param question:
        :return:
        """
        word_objects = self.tw.get_word_objects(question)
        queries_dict = dict()

        for rule in self.rules:
            #print(rule)
            # word_objects是一个列表，元素为是包含词语和词语对应词性的对象
            query, num = rule.apply(word_objects)

            if query is not None:
                queries_dict[num] = query

        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            return list(queries_dict.values())[0]
        else:
            # TODO 匹配多个语句，以匹配关键词最多的句子作为返回结果
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[1])
            return sorted_dict[0][1]

if __name__ == '__main__':
    q2s = Question2Sparql(['./dict/disease_pos.txt', './dict/medicine_pos.txt','./dict/symptom_pos.txt', './dict/therapy_pos.txt', './dict/examination_pos.txt'])
    question = 'CT是什么'
    my_query = q2s.get_sparql(question.encode('utf-8'))
    print(my_query)
