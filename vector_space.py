#Arushi Dogra

from gensim.models import Word2Vec
import numpy
#without ic

sent1 = raw_input()
sent2 = raw_input()

sent1=sent1.split()
sent2=sent2.split()
model = Word2Vec.load_word2vec_format('deps.words', binary=False)

for i in sent1:
    try:
        mat1=mat1+model[i]
    except:
        mat1=model[i]

for i in sent2:
    try:
        mat2=mat2+model[i]
    except:
        mat2=model[i]

print "Similarity is : " + str(numpy.dot(mat1,mat2))
