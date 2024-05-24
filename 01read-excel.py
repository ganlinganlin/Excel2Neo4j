# -*- coding =utf-8 -*-
import numpy as np
import pandas as pd
import csv
df = pd.read_excel('数据统计与分析基础-大数据分析与可视化-海量数据挖掘.xlsx')
a=['']*7
tag=0
head2={"text":'',"label":'',"subject":'',"cognition":''}
head={"text":'',"label":'',"subject":'',"cognition":''}
tail={"text":'',"label":'',"subject":'',"cognition":''}

#遍历前7列生成包含关系三元组
for index, row in df.iterrows():
    for i in range(0,7):
        if pd.notna(row[i]):
            a[i]=row[i]   #寻找结点名字
            tag=i         #查询节点所在位置
            if i==0:
                head2["text"] =row[i]
                head2["label"]='level_'+str(i+1)+'_kP'
                # if pd.notna(row[14]):
                #     head2["subject"] =row[14]
                # if pd.notna(row[11]):
                #     head2["cognition"] =row[11]
            else:
                if i==1:

                    head["text"] =  head2["text"]
                    head["label"] = head2["label"]
                    head["subject"] = head2["subject"]
                    head["cognition"] = head2["cognition"]

                else:
                    head["text"] = a[i-1]
                    head["label"] = 'level_'+str(i) + '_kP'
                    head["subject"] = tail["subject"]
                    if tail["cognition"]:
                        head["cognition"] = tail["cognition"]
                tail["text"] = row[i]
                tail["label"] = 'level_'+str(i+1)+ '_kP'
                # head2["text"] = a[i-1]
                # head2["label"] = 'level_'+str(i) + '_kP'
                # if pd.notna(row[14]):
                #     head2["subject"] =row[14]
                # if pd.notna(row[11]):
                #     head2["cognition"] =row[11]
                # if pd.notna(row[14]):
                #     tail["subject"] =row[14]
                # else:
                #     tail["subject"] = ''
                # if pd.notna(row[11]):
                #     tail["cognition"] =row[11]
                # else:
                #     tail["cognition"] = ''
                data = [head, '包含', tail ,","]
                f=open('triple.csv','a',newline='',encoding='utf-8')
                with f as csvf:
                    writer=csv.writer(csvf)
                    writer.writerow(data)
                    csvf.close()
            break

#生成前置知识三元组
for index, row in df.iterrows():
    #print(row[7])
    if pd.notna(row[7]):
        roww=row[7].split(';')
        for s in roww:
            for i in range(6,-1,-1):

                if pd.notna(row[i]):
                    tail['text']=s
                    tag=0
                    for index1, row1 in df.iloc[index-1::-1].iterrows():
                        for j in range(6,-1,-1):
                            if s==row1[j]:
                                tail["label"] = 'level_' + str(j + 1) + '_kP'
                                if pd.notna(row1[14]):
                                    tail["subject"] =row1[14]
                                else:
                                    tail["subject"] = ''
                                if pd.notna(row1[11]):
                                    tail["cognition"] =row1[11]
                                else:
                                    tail["cognition"] = ''
                                tag=1
                                break
                        if tag==1:
                            break
                    head["text"] = row[i]
                    head["label"] = 'level_'+str(i+1)+ '_kP'
                    # if pd.notna(row[14]):
                    #     head["subject"] =row[14]
                    # else:
                    #     head["subject"] = ''
                    # if pd.notna(row[11]):
                    #     head["cognition"] =row[11]
                    # else:
                    #     head["cognition"] = ''
                    data = [head, '前置知识', tail]
                    f=open('triple.csv','a',newline='',encoding='utf-8')
                    with f as csvf:
                        writer=csv.writer(csvf)
                        writer.writerow(data)
                        csvf.close()
                    break



#生成关联知识三元组
for index, row in df.iterrows():
    #print(row[9])
    if pd.notna(row[9]):
        roww=row[9].split(';')
        for s in roww:
            for i in range(6,-1,-1):

                if pd.notna(row[i]):
                    tail['text']=s
                    tag=0
                    for index1, row1 in df.iloc[index-1::-1].iterrows():
                        for j in range(6,-1,-1):
                            if s==row1[j]:
                                tail["label"] = 'level_' + str(j + 1) + '_kP'
                                if pd.notna(row1[14]):
                                    tail["subject"] =row1[14]
                                else:
                                    tail["subject"] = ''
                                if pd.notna(row1[11]):
                                    tail["cognition"] =row1[11]
                                else:
                                    tail["cognition"] = ''
                                tag=1
                                break
                        if tag==1:
                            break
                    head["text"] = row[i]
                    head["label"] = 'level_'+str(i+1)+ '_kP'
                    # if pd.notna(row[14]):
                    #     head["subject"] =row[14]
                    # else:
                    #     head["subject"] = ''
                    # if pd.notna(row[11]):
                    #     head["cognition"] =row[11]
                    # else:
                    #     head["cognition"] = ''
                    data = [head, '关联知识', tail]
                    f=open('triple.csv','a',newline='',encoding='utf-8')
                    with f as csvf:
                        writer=csv.writer(csvf)
                        writer.writerow(data)
                        csvf.close()
                    break