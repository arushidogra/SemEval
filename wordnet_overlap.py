from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis

def max(a,b):
    if(a>b):
        return a
    else:
	return b

sent1 = raw_input()
sent2 = raw_input()

sent1=sent1.split()
sent2=sent2.split()
score1={}
score2={}

for i in sent1:
	score1[i]=1

for i in sent2:
	score2[i]=1

for i in sent2:
    try:
        score1[i]=score1[i]
    except:
	w = wn.synsets(i)
	wbar = []
	for j in sent1:
	    wbar.append(wn.synsets(j))
    score1[i]=0
    for p in w:
        for j in wbar:
            for k in j:
         	score1[i]=max(score1[i],p.path_similarity(k))


for i in sent1:
    try:
	score2[i]=score2[i]
    except:
	w = wn.synsets(i)
	wbar = []
	for j in sent2:
	    wbar.append(wn.synsets(j))
    score2[i]=0
    for p in w:
        for j in wbar:
            for k in j:
         	score2[i]=max(score2[i],p.path_similarity(k))


pws1s2=0
pws2s1=0

for i in sent1:
    pws1s2=pws1s2+score2[i]

for i in sent2:
    pws2s1=pws2s1+score1[i]

# Word Net augmented word overlap feature WNAF
wnaf = (pws2s1*pws1s2)/(pws1s2+pws2s1)
print "Word Net augmented word overlap feature WNAF is : " + str(wnaf)
