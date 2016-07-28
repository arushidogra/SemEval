from nltk.util import ngrams
from nltk.corpus import stopwords
stop = stopwords.words('english')
n = input()
sent1=raw_input()
sent2=raw_input()


# Without removing stop words
sent1_bi = set(ngrams(sent1.split(),n))
sent2_bi = set(ngrams(sent2.split(),n))
s1 = len(sent1_bi)
s2 = len(sent2_bi)
s1Is2 = len(sent1_bi.intersection(sent2_bi));
ngo = 2*pow((s1/s1Is2)+(s2/s1Is2),-1)
print ngo

#removing stopwords

sent1_l = [i for i in sent1.split() if i not in stop]
sent2_l = [i for i in sent2.split() if i not in stop]

sent1= ""
for i in sent1_l:
    sent1 = sent1 + " " + i
sent2= ""
for i in sent2_l:
    sent2 = sent2 + " " + i
sent1_bi = set(ngrams(sent1.split(),n))
sent2_bi = set(ngrams(sent2.split(),n))
s1 = len(sent1_bi)
s2 = len(sent2_bi)
s1Is2 = len(sent1_bi.intersection(sent2_bi));
if(s1Is2!=0):
    try:
        ngo = 2*pow((s1/s1Is2)+(s2/s1Is2),-1)
        print ngo
    except :
        print "haha"
else:
    print 0
