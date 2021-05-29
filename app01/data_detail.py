#-*- coding:utf-8 -*-
from collections import Counter
from jieba import analyse
import time
import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from app01 import models, data_list


def avg(x):
    info = {}

    if x[-3] == '万':
        k = 10000;
    elif x[-3] == '千':
        k = 1000;
    else:
        k = 1;
    bottomSalary= 0
    topSalary = 0
    position = x.find('-')
    length = len(x)
    if position != -1:  # 处理有‘···k-···k’的薪资上下限
        bottomSalary = float(x[:position]) * k
        topSalary = float(x[position + 1:length - 3]) * k

    if x[-1] == '年':
        bottomSalary = bottomSalary / 12
        topSalary = topSalary / 12
    elif x[-1] == '天':
        bottomSalary = bottomSalary * 30
        topSalary = topSalary * 30

    info['bottomSalary'] = bottomSalary/1000
    info['topSalary'] = topSalary/1000
    info['avgSalary'] = (bottomSalary + topSalary) / 2000

    return info

class HandleLagouData(object):
    def __init__(self):
        self.date = time.strftime("%Y-%m-%d",time.localtime())

    def get_joblist(self):
        data = models.custom.objects.all()
        data = [{"job_href": x.job_href, "job_name": x.job_name,
                          "companytype_text": x.companytype_text, "jobwelf_list": x.jobwelf_list,
                          "degreefrom": x.degreefrom, "company_name": x.company_name,
                          "workyear": x.workyear, "companysize_text": x.companysize_text,
                          "companyind_text": x.companyind_text, "providesalary_text": x.providesalary_text, }
                         for x in data]
        #学历和工作年限数据转换
        for i in range(len(data)):
            data[i]["degreefrom"]=list(data_list.degreefrom_l.values())[list(data_list.degreefrom_l.keys()).index('0'+data[i]['degreefrom']+'0')]
            data[i]["workyear"]=list(data_list.workyear_l.values())[list(data_list.workyear_l.keys()).index('0'+data[i]['workyear']+'0')]

        return data

    def query_industryfield_result(self):
        info = {}
        data = models.custom.objects.all().values('companyind_text')
        data = [x['companyind_text'] for x in data if x['companyind_text'] != '']
        list = []
        for i in data:
            for j in i.split('/'):
                list.append(j)

        result_list1 = [x for x in list]
        result_list2 = [x for x in Counter(result_list1).items()]
        data = [{"name": x[0], "value": x[1]} for x in result_list2 if x[1]>4]
        name_list = [name['name'] for name in data]
        info['x_name'] = name_list
        info['data'] = data

        return info

    # 查询薪资情况
    def query_salary_result(self):
        info = {}
        data = models.custom.objects.all().values('providesalary_text')
        data = [avg(x['providesalary_text']) for x in data if x['providesalary_text'] != '']
        name_list = []
        for i in range(len(data)):
            name_list.append(i+1)
        # 先用name再用value排序
        result1 = sorted(data, key=lambda x: (x['avgSalary'], x['bottomSalary'], x['topSalary']))
        name_list1 = [result1['topSalary'] for result1 in result1]
        name_list2 = [result1['bottomSalary'] for result1 in result1]
        name_list3 = [result1['avgSalary'] for result1 in result1]
        info['x_name'] = name_list
        info['top']= name_list1
        info['bottom'] = name_list2
        info['avg'] = name_list3

        #计算平均数
        s = 0
        for i in range(len(name_list3)):
            s += name_list3[i]
        s = s/len(name_list3)
        #计算众数
        maxkey_list = [x for x in Counter(name_list3).items()]
        maxkey = sorted(maxkey_list, key=lambda x: (x[1]), reverse=True)

        info['salary'] = {
            'avg':s,
            'num':maxkey[0],
        }
        return (info)

    # 查询工作年限情况
    def query_workyear_result(self):
        info = {}
        data = models.custom.objects.all().values('workyear')
        data = [x['workyear'] for x in data] #if x['workyear'] != '']
        data = np.char.replace(data, '','0')
        data = [list(data_list.workyear_l.values())[list(data_list.workyear_l.keys()).index(i)] for i in data]

        result = pd.Series(data)
        # 处理原始数据
        result_list1 = [x for x in result]
        # 计数,并返回
        result_list2 = [x for x in Counter(result_list1).items()]
        result = [{"name": x[0], "value": x[1]} for x in result_list2]
        name_list = [name['name'] for name in result]
        info['x_name'] = name_list
        info['data'] = result

        return info

    # 查询学历信息
    def query_education_result(self):
        info = {}
        data = models.custom.objects.all().values('degreefrom')
        data = [x['degreefrom'] for x in data ] #if x['degreefrom'] != '' ]
        data = np.char.replace(data, '','0')
        data = [list(data_list.degreefrom_l.values())[list(data_list.degreefrom_l.keys()).index(i)] for i in data]

        result = pd.Series(data)

        # 处理原始数据
        result_list1 = [x for x in result]
        # 计数,并返回
        result_list2 = [x for x in Counter(result_list1).items()]
        result = [{"name": x[0], "value": x[1]} for x in result_list2]
        name_list = [name['name'] for name in result]
        info['x_name'] = name_list
        info['data'] = result
        return info

    # 职业名称,横向柱状图
    def query_custom_result(self):
        info = {}

        result = self.data['职位名称']
        # 处理原始数据
        result_list1 = [x for x in result]
        # 计数,并返回
        result_list2 = [x for x in Counter(result_list1).items()]
        result = [{"name": x[0], "value": x[1]} for x in result_list2]
        name_list = [name['name'] for name in result]
        info['x_name'] = name_list
        info['data'] = result

        return info

    def query_city_result(self):
        info = {}
        data1 = models.custom.objects.all().values('workarea_text', 'providesalary_text')
        data = [[x['workarea_text'],x['providesalary_text']] for x in data1 if x['workarea_text'] != '异地招聘']
        list = []
        for i in data:
            x = 0
            for j in i[0].split('-'):
                if x == 0:
                    list.append(j)
                x = 2
        result_list2 = [x for x in Counter(list).items()]

        list2 = []
        for i in result_list2:
            all_s = [avg(x['providesalary_text']) for x in data1 if x['workarea_text'] == i[0] and x['providesalary_text'] != '']
            name_list3 = [x['avgSalary'] for x in all_s]
            if len(name_list3) != 0:
                # 计算平均数
                s = 0
                for j in range(len(name_list3)):
                    s += name_list3[j]
                s = s / len(name_list3)
                list2.append([i[0],i[1],round(s,2)])

        info['x_name_city'] = [{"name": x[0], "value": x[1]} for x in list2]
        info['x_name_avg'] = [{"name": x[0], "value": x[2]} for x in list2]
        info['x_name'] = [name['name'] for name in info['x_name_city']]

        return info

    #融资情况
    def query_financestage_result(self):
        info = {}
        data = models.custom.objects.all().values('companytype_text')
        data = [x['companytype_text'] for x in data if x['companytype_text'] != '']
        result = pd.Series(data)
        # 处理原始数据
        result_list1 = [x for x in result ]
        # 计数,并返回
        result_list2 = [x for x in Counter(result_list1).items()]
        result = [{"name": x[0], "value": x[1]} for x in result_list2]
        name_list = [name['name'] for name in result]
        info['x_name'] = name_list
        info['data'] = result
        return info

    # 公司规模
    def query_companysize_result(self):
        info = {}
        data = models.custom.objects.all().values('companysize_text')
        data = [x['companysize_text'] for x in data if x['companysize_text'] != '']
        result = pd.Series(data)
        # 处理原始数据
        result_list1 = [x for x in result]
        # 计数,并返回
        result_list2 = [x for x in Counter(result_list1).items()]
        result = [{"name": x[0], "value": x[1]} for x in result_list2]
        name_list = [name['name'] for name in result]
        info['x_name'] = name_list
        info['data'] = result
        return info

    #福利标签云图
    def query_tag_result(self):
        data = models.Job.objects.all().values('jobwelf_list')
        data = [x['jobwelf_list'] for x in data if x['jobwelf_list'] != '']
        # 处理原始数据
        data1 = str(data).replace("\"", "").replace(" ", "") \
            .replace("'", "").replace("[", "").replace("]", "").replace(",,,", ",")
        wordcloud = WordCloud(font_path='msyh.ttc', height=400, width=600, background_color='white')
        wordcloud.generate(data1)
        plt.imshow(wordcloud)
        wordcloud.to_file('static/img/detail_key.jpg')
        plt.axis("off")
        return data1

data_a = HandleLagouData()
