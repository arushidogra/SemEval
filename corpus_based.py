from gensim.models import Word2Vec
import numpy
word1 = raw_input()
word2 = raw_input()

model = Word2Vec.load_word2vec_format('deps.words', binary=False)
print "Cosine Sim is : " + str(numpy.dot(model[word1],model[word2]))

#http://www1.se.cuhk.edu.hk/~seem5680/lecture/LSI-Eg.pdf
#http://blog.josephwilk.net/projects/latent-semantic-analysis-in-python.html
