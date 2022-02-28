"""
@desc: 为每个问题设定语义模板
"""
from refo import finditer, Predicate, Star, Any, Disjunction
import re
import random




# TODO SPARQL前缀和模板
SPARQL_PREXIX = u"""
PREFIX : <http://bckg.org:8086#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
"""
SPARQL_SELECT_TEM = u"{prefix}\n" + \
             u"SELECT DISTINCT {select} WHERE {{\n" + \
             u"{expression}\n" + \
             u"}}\n"

class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        # 正则表达式
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token.decode('utf-8'))
        m2 = self.pos.match(word.pos)
        return m1 and m2

class Rule(object):
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action
        self.condition_num = random.random()

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])

        return self.action(matches), self.condition_num

class QuestionSet:
    def __init__(self):
        pass
    #todo 疾病
    @staticmethod
    def DisSym(word_objects):
        """
        1.某疾病有什么症状？DisSym
        """
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :疾病相关症状 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break
        return sparql

    @staticmethod
    def DisDis1(word_objects):
        '''
        2.1 某疾病有什么并发症？DisDis1
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :疾病并发症 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisDis2(word_objects):
        '''
        2.2 某疾病分期？DisDis2
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :分期 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisDis3(word_objects):
        '''
        2.3 某疾病分类？DisDis3
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :分类 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisDis4(word_objects):
        '''
        2.4 某疾病分级？DisDis4
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :分级 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisDis5(word_objects):
        '''
        2.5 某疾病分型？DisDis5
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :分子分型 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisExa(word_objects):
        '''
        3. 疾病相关检查  DisExa
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :疾病相关检查 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisExa1(word_objects):
        '''
        3.1 影像学检查  DisExa1
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :影像学检查 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisExa2(word_objects):
        '''
        3.2 辅助检查  DisExa2
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :辅助检查 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisExa3(word_objects):
        '''
        3.3 内窥镜检查  DisExa3
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :内窥镜检查 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisThe(word_objects):
        '''
        4 疾病-疾病相关治疗  DisThe
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :疾病相关治疗 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisThe1(word_objects):
        '''
        4.1 疾病-手术治疗  DisThe1
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :手术治疗 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisThe2(word_objects):
        '''
        4.2 疾病-化疗  DisThe2
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :化疗 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisThe3(word_objects):
        '''
        4.3 疾病-放疗  DisThe3
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :放疗 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisThe4(word_objects):
        '''
        4.4 疾病-辅助治疗  DisThe4
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis:
                e = u":{Query} :辅助治疗 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def SymDis(word_objects):
        '''
        SymDis 5 症状相关疾病
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosSym:
                e = u":{Query} :症状相关疾病 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def SymAna(word_objects):
        '''
        SymAna 6 症状相关部位
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosSym:
                e = u":{Query} :症状相关部位 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def SymSym(word_objects):
        '''
        SymSym  7 症状相关症状
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosSym:
                e = u":{Query} :症状相关症状 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def TheDis(word_objects):
        '''
        TheDis 8 治疗并发症
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosThe:
                e = u":{Query} :治疗并发症 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def TheMed(word_objects):
        '''
        TheMed  9 治疗相关药物
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosThe:
                e = u":{Query} :治疗相关药物 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def TheAna(word_objects):
        '''
        TheAna  10 治疗相关部位
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosThe:
                e = u":{Query} :治疗相关部位 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def ExaAna(word_objects):
        '''
        ExaAna 11 检查相关部位
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosExa:
                e = u":{Query} :检查相关部位 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def ExaDis(word_objects):
        '''
        ExaDis  12 检查相关疾病
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosExa:
                e = u":{Query} :检查相关疾病 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def ExaMed(word_objects):
        '''
        ExaMed 13 检查相关药物
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosExa:
                e = u":{Query} :检查相关药物 ?o." \
                    u"?o rdfs:label ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql

    @staticmethod
    def DisMea(word_objects):
        '''
        DisMea 14 疾病概述
        '''
        select = u"?x"

        sparql = None
        for w in word_objects:
            if w.pos == PosDis or w.pos == PosExa or w.pos == PosMed or w.pos == PosSym or w.pos == PosThe:
                e = u":{Query} :概述 ?x".format(Query=w.token.decode('utf-8'))

                sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                                  select=select,
                                                  expression=e)
                break

        return sparql



# TODO 定义关键词
# 药品、疾病词性
PosDis = 'nd'
DisEntity = (W(pos=PosDis))

PosMed = 'nm'
MedEntity = (W(pos=PosMed))

PosSym = 'ns'
SymEntity = (W(pos=PosSym))

PosThe = 'nt'
TheEntity = (W(pos=PosThe))

PosExa = 'ne'
ExaEntity = (W(pos=PosExa))

#问题关键词
SymptomKey = (W('症状')|W('症候')|W('特征')|W('临床表现')|W('临床症状')|W('表现'))
ComplicationKey = (W('病发症')|W('并发症'))
StageKey = (W('分期')|W('阶段'))
ClassificationKey = (W('分类')|W('组织学分类'))
GradingKey = (W('分级')|W('组织学分级'))
TypingKey = (W('分型')|W('分子分型'))
ExaminationKey = (W('检查')|W('检验')|W('化验')|W('查')|W('测'))
ImagingKey = (W('影像学')|W('影像学检查')|W('影像'))
EndoscopeKey = (W('内窥镜')|W('内窥镜检查')|W('内镜')|W('内镜检查')|W('膀胱镜')|W('膀胱镜检查'))
AccessoryExaKey = (W('辅助检查')|W('其他检查')|W('其它检查'))
TherapyKey = (W('治')|W('治疗')|W('治疗措施'))
OperationKey = (W('手术')|W('手术治疗'))
ChemotherapyKey = (W('化疗')|W('化学治疗')|W('化学'))
RadiotherapyKey = (W('放疗')|W('放射治疗')|W('放射'))
AdjuvantTheKey = (W('辅助治疗')|W('其他治疗')|W('其它治疗'))
DieaseKey = (W('病')|W('疾病'))
AnatomyKey = (W('部位')|W('器官')|W('身体'))
MedicineKey = (W('药')|W('药品')|W('药治')|W('药治疗'))
MeanKey = (W('含义')|W('概述')|W('意思')|W('意义')|W('内容')|W('什么'))

yufang_keyword = (W('预防')|W('预防措施'))
gaishu_keyword = (W('概述'))
gnzhzh_keyword = (W('功效')|W('疗效')|W('用处')|W('用'))
pzwh_keyword = (W('批准文号')|W('文号'))
symptom_disease_keyword = (W('病')|W('疾病'))
#规则集合
rules = [
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + SymptomKey + Star(Any(),greedy=False),action=QuestionSet.DisSym),#1. 疾病-症状
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + ComplicationKey + Star(Any(),greedy=False),action=QuestionSet.DisDis1),#2.1 疾病-并发症
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + StageKey + Star(Any(),greedy=False),action=QuestionSet.DisDis2),#2.2 疾病-分期
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + ClassificationKey + Star(Any(),greedy=False),action=QuestionSet.DisDis3),#2.3 疾病-分类
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + GradingKey + Star(Any(),greedy=False),action=QuestionSet.DisDis4),#2.4 疾病-分类
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + TypingKey + Star(Any(),greedy=False),action=QuestionSet.DisDis4),#2.5 疾病-分子分型
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + ExaminationKey + Star(Any(),greedy=False),action=QuestionSet.DisExa),#3. 疾病-检查
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + ImagingKey + Star(Any(),greedy=False),action=QuestionSet.DisExa1),#3.1 疾病-影像学检查
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + EndoscopeKey + Star(Any(),greedy=False),action=QuestionSet.DisExa2),#3.2 疾病-内窥镜检查
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + AccessoryExaKey + Star(Any(),greedy=False),action=QuestionSet.DisExa3),#3.3 疾病-辅助检查
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + TherapyKey + Star(Any(),greedy=False),action=QuestionSet.DisThe),#4 疾病-治疗
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + OperationKey + Star(Any(),greedy=False),action=QuestionSet.DisThe1),#4.1 疾病-手术治疗
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + ChemotherapyKey + Star(Any(),greedy=False),action=QuestionSet.DisThe2),#4.2 疾病-化疗
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + RadiotherapyKey + Star(Any(),greedy=False),action=QuestionSet.DisThe3),#4.3 疾病-放疗
    Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + AdjuvantTheKey + Star(Any(),greedy=False),action=QuestionSet.DisThe4),#4.4 疾病-辅助治疗
    Rule(condition_num=2,condition=SymEntity + Star(Any(),greedy=False) + DieaseKey + Star(Any(),greedy=False),action=QuestionSet.SymDis),#5 症状相关疾病
    Rule(condition_num=2, condition=SymEntity + Star(Any(), greedy=False) + AnatomyKey + Star(Any(), greedy=False),action=QuestionSet.SymAna),  # 6 症状相关部位
    Rule(condition_num=2, condition=SymEntity + Star(Any(), greedy=False) + SymptomKey + Star(Any(), greedy=False),action=QuestionSet.SymSym),  # 7 症状相关症状
    Rule(condition_num=2,condition=TheEntity + Star(Any(),greedy=False) + DieaseKey + Star(Any(),greedy=False),action=QuestionSet.TheDis),#8 治疗并发症
    Rule(condition_num=2, condition=TheEntity + Star(Any(), greedy=False) + MedicineKey + Star(Any(), greedy=False),action=QuestionSet.TheMed),  # 9 治疗相关药物
    Rule(condition_num=2, condition=TheEntity + Star(Any(), greedy=False) + AnatomyKey + Star(Any(), greedy=False),action=QuestionSet.TheAna),  # 10 治疗相关部位
    Rule(condition_num=2,condition=ExaEntity + Star(Any(),greedy=False) + AnatomyKey + Star(Any(),greedy=False),action=QuestionSet.ExaAna),#11 检查相关部位
    Rule(condition_num=2, condition=ExaEntity + Star(Any(), greedy=False) + DieaseKey + Star(Any(), greedy=False),action=QuestionSet.ExaDis),  # 12 检查相关疾病
    Rule(condition_num=2, condition=ExaEntity + Star(Any(), greedy=False) + MedicineKey + Star(Any(), greedy=False),action=QuestionSet.ExaMed),  # 13 检查相关药物
    #Rule(condition_num=2, condition=DisEntity + Star(Any(), greedy=False) + MeanKey + Star(Any(), greedy=False),action=QuestionSet.DisMea),  # 14 疾病概述
    Rule(condition_num=2, condition=Star(Any(), greedy=False) + MeanKey + Star(Any(), greedy=False),action=QuestionSet.DisMea),  # 14 概述

    #Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False) + gaishu_keyword + Star(Any(),greedy=False),action=QuestionSet.has_gaishu_question),
    #治疗Rule(condition_num=2,condition=DisEntity + Star(Any(), greedy=False) +zhiliao_keyword,action=QuestionSet.DIS_THE),
    #治疗Rule(condition_num=2, condition=Star(Any(), greedy=False) + zhiliao_keyword + DisEntity,action=QuestionSet.DIS_THE),
    #Rule(condition_num=2,condition=Star(Any(),greedy=False) + yufang_keyword + DisEntity,action=QuestionSet.has_yufang_question),


    #Rule(condition_num=2,condition=PosMed + Star(Any(),greedy=False) + gnzhzh_keyword +  Star(Any(),greedy=False) ,action=QuestionSet.has_gnzhzh_question),
    #Rule(condition_num=2,condition=PosMed + Star(Any(),greedy=False) + pzwh_keyword + Star(Any(),greedy=False),action=QuestionSet.has_pzwh_question),

    #Rule(condition_num=2,condition=SymEntity + Star(Any(),greedy=False) + gaishu_keyword + Star(Any(),greedy=False),action=QuestionSet.has_sympotm_gaishu_question),
    #Rule(condition_num=2,condition=SymEntity + Star(Any(),greedy=False) + yufang_keyword + Star(Any(),greedy=False),action=QuestionSet.has_sympotm_yufang_question),
    #Rule(condition_num=2,condition=Star(Any(),greedy=False) + yufang_keyword + SymEntity,action=QuestionSet.has_sympotm_yufang_question),

    #Rule(condition_num=2,condition=DisEntity + Star(Any(),greedy=False)  + disease_drug_keyword + (Star(Any(),greedy=False)|DisEntity),action=QuestionSet.has_disease_to_drug_question),
    #Rule(condition_num=2,condition=Star(Any(),greedy=False) + disease_drug_keyword + Star(Any(),greedy=False) + DisEntity,action=QuestionSet.has_disease_to_drug_question),
    #Rule(condition_num=2,condition=SymEntity + Star(Any(),greedy=False) + symptom_disease_keyword,action=QuestionSet.has_symptom_to_disease_question),

]



