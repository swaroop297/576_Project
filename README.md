# 576_Project | Group 24 - NLP Project

# Description for the files in the repo

jsonCreator.py - Creates JSON objects of the format:

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
             
qasrl_input_generator.py - Generate JSONL files are required by QA-SRL module. 

Ex: {"sentence" : "He doesn't fit in the treehouse because he's too big"} 

knowledgeInput_qasrl.jsonl - JSONL file for the Knowledge Sentences
wscInput_qasrl.jsonl - JSONL file for the WSC sentences

knowledge_sentences.xlsx - File with WSC sentences and Knowledge sentences - Input for jsonCreator.py and qasrl_input_generator.py and 

query_generator.py - Takes input sentences for an Excel files and writes query sentences to an output text file. 

wsc_sentences.txt - WSC sentence in Text format

wsc_qa.txt - Output of QA-SRL for the WSC sentences

wsc_final.py - Appends WSC sentences with its QA-SRL output. 
