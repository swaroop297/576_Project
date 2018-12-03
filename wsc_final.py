wsc = []
wsc_qa = []
wsc_out = []
with open("wsc_sentences.txt") as f:
    for line in f:
        	wsc.append(line)
with open("wsc_qa.txt") as g:
	for line1 in g:
		wsc_qa.append(line1)
print(len(wsc))
print(len(wsc_qa))	
for i,k in zip(wsc,wsc_qa):
	wsc_out.append(i.strip()+"$$$$"+k.strip()+"\n")
f = open("final_wsc.txt", "w+")
for i in wsc_out:
    f.write(str(i))
f.close()
