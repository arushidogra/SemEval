import nltk
import math

s1 = raw_input()
s2 = raw_input()

a = open("test.txt","r")
corpus = a.read()
tokens = nltk.word_tokenize(corpus)

dic={}
total=0
for i in tokens:
    total=total+1
    try :
        dic[i]=dic[i]+1
    except:
        dic[i]=1

ic={}
s1=nltk.word_tokenize(s1)
s2=nltk.word_tokenize(s2)
set_s1=set(s1)
set_s2=set(s2)
inte = set_s1.intersection(set_s2)

for i in s1:
    try:
        ic[i]=math.log(total,2.71828)-math.log(dic[i],2.71828)
    except:
        ic[i]=math.log(total,2.71828)
for i in s2:
    try:
        ic[i]=math.log(total,2.71828)-math.log(dic[i],2.71828)
    except:
        ic[i]=math.log(total,2.71828)



num=0
den1=0
den2=0
for i in inte:
    num=num+ic[i]
for i in s2:
    den1 = den1+ic[i]
for i in s1:
    den2 = den2+ic[i]

wwcs1s2=float(num)/den1
wwcs2s1=float(num)/den2

#The weighted word overlap between two sentences
#is calculated as the harmonic mean of the
#wwc(S1, S2) and wwc(S2, S1).

wwoc =(wwcs1s2*wwcs1s2)/(wwcs1s2+wwcs1s2)
print wwoc

