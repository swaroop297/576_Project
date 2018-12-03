import re
import csv
import pandas
import json

df = pandas.read_excel("knowledge_sentences.xlsx")
df = df.fillna(' ')

wsc  = df['WSC Problems'].values.tolist()
print(len(wsc))
f = open("wscInput_qasrl.jsonl", "w+")
for i in wsc:
    f.write('{"sentence" : "%s"} \n' % str(i).replace('\n', '').replace('"','\\"'))
f.close()

knowledge  = df['Knowledge Sentence'].values.tolist()
print(len(knowledge))
f = open("knowledgeInput_qasrl.jsonl", "w+")
for i in knowledge:
    f.write('{"sentence" : "%s"} \n' % str(i).replace('\n', '').replace('"','\\"'))
f.close()
