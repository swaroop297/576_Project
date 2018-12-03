import csv
import json
import spacy

with open("wsc.txt") as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

mysentArr = []

county =0
wsc_sent = []
for i in content:
    if county < 289:
        temp = i.split(":")
#        print(temp[1].split("}")[0])
        valMe = (temp[1].split("}")[0])
        print(valMe)
        valMe = valMe.replace("\"", '')
        wsc_sent.append(valMe)
 #       print("WSC SENT: ", valMe)
        county = county + 1


csvfile1 = open('Project_Group24 - all_WSC_data.csv', 'r',  encoding="utf8")

nlp = spacy.load('en_core_web_sm')
jsonfile = open('Output.json', 'w')

fieldnames = ("sl_no","ws_sent","Pronoun","AnswerOption","Present","search_query","know_sent","know_url")
reader = csv.DictReader( csvfile1, fieldnames)
out = json.dumps( [ row for row in reader ] )
myJson = json.loads(out)

count =0

answer= []
choice1 =[]
choice2 =[]
know_sent= []
know_url = []
pronoun =[]
search_query = []

for i in myJson:
    if i['ws_sent'] is not '' and count < 290 and count > 0:
        print(i['ws_sent'])
        new = i['ws_sent'].split(":")[1]
         #print(new)
        res = nlp(new)
  #      print("Answer Options:", i['AnswerOption'])
  #      print("Answer Options:")
  #      print("Choice 1", i['AnswerOption'].split(',')[0])
  #      print("Choice 2", i['AnswerOption'].split(',')[1].replace(' ', '', 1))
        choice1.append(i['AnswerOption'].split(',')[0])
        choice2.append(i['AnswerOption'].split(',')[1])
        ans =''
        temp = str(i['search_query'])
  #     temp =temp.replace('\\','')
        temp = temp.replace("\"", '')
        search_query.append(temp)
        know_sent.append(i['know_sent'])
        know_url.append(i['know_url'])
        pronoun.append(i['Pronoun'])

        for token in res:
          if token.pos_ is 'NOUN':
             ans = ans + token.text + " "
           #  print(token.pos_, token)
          elif token.pos_ is 'PROPN':
              ans = ans + token.text + " "
           #   print(token.pos_, token)
          elif token.pos_ is 'CCONJ':
             ans = ans + token.text + " "
            # print(token.pos_, token)
    #    print(ans)   # Has the Answer
        answer.append(ans)
        count = count +1
    elif count is 0 :
        count = count +1

count = 0
proCount = 0
for i in content:
     if count < 289:
       #print(content[count])
       # wsc_sent.append(content[count])
        moc = nlp(content[count])

        proList = []
        for token in moc:
             if token.pos_ is "PRON":
                  proList.append(token.text)
                  proCount = proCount + 1
                #  print("Pronoun: ", token.text, "  ", token.pos_)
        count = count + 1

doc = nlp(myJson[2]["ws_sent"])

data = {
  'ans': 'The city councilmen',
  'choice1': 'The city councilmen',
  'choice2': 'The demonstrators',
  'know_sent': 'NA',
  'know_url': 'NA',
  'pronoun': 'they',
  'search_query': 'NA',
  'ws_sent': 'The city councilmen refused the demonstrators a permit because '
             'they feared violence.'}

json_data = json.dumps(data)

count =0
final_jsonData =[]
for x in range(0, 289):
    final_data = {
                'ans': (answer[x]),
                'choice1': (choice1[x]),
                'choice2': (choice2[x]),
                'know_sent': (know_sent[x]),
                'know_url': (know_url[x]),
                'pronoun': (pronoun[x]),
                'search_query': (search_query[x]),
                'ws_sent': (wsc_sent[x])}
    final_jsonData.append(final_data)

print(final_jsonData)

with open('output.json', 'w') as outfile:
    json.dump(final_jsonData, outfile)
