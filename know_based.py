from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus import genesis

genesis_ic = wn.ic(genesis, False, 0.0)
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
brown_ic = wordnet_ic.ic('ic-brown.dat')

def max(a,b):
	if a>b:
		return a
	else:
		return b

word1 = raw_input()
word2 = raw_input()


word1 = wn.synsets(word1)
word2 = wn.synsets(word2)


#synset1.path_similarity(synset2): Return a score denoting how similar two word senses are, based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy. The score is in the range 0 to 1. By default, there is now a fake root node added to verbs so for cases where previously a path could not be found---and None was returned---it should return a value. The old behavior can be achieved by setting simulate_root to be False. A score of 1 represents identity i.e. comparing a sense with itself will return 1
path_sim=0
for i in word1:
    for j in word2:
        try:
            path_sim=max(path_sim,i.path_similarity(j))
        except:
            continue
print "Path Similarity is : " + str(path_sim)

#synset1.lch_similarity(synset2): Leacock-Chodorow Similarity: Return a score denoting how similar two word senses are, based on the shortest path that connects the senses (as above) and the maximum depth of the taxonomy in which the senses occur. The relationship is given as -log(p/2d) where p is the shortest path length and d the taxonomy depth
lch_sim=0
for i in word1:
    for j in word2:
        try:
            lch_sim=max(lch_sim,i.lch_similarity(j))
        except:
            continue
print "Lch Similarity is : " + str(lch_sim)

#synset1.wup_similarity(synset2): Wu-Palmer Similarity: Return a score denoting how similar two word senses are, based on the depth of the two senses in the taxonomy and that of their Least Common Subsumer (most specific ancestor node).
wup_sim=0
for i in word1:
    for j in word2:
        try:
            wup_sim=max(wup_sim,i.wup_similarity(j))
        except:
            continue
print "Wup Similarity is : " + str(wup_sim)

#synset1.res_similarity(synset2, ic): Resnik Similarity: Return a score denoting how similar two word senses are, based on the Information Content (IC) of the Least Common Subsumer (most specific ancestor node). Note that for any similarity measure that uses information content, the result is dependent on the corpus used to generate the information content and the specifics of how the information content was created.
res_sim=0
for i in word1:
    for j in word2:
        try:
            res_sim=max(res_sim,i.res_similarity(j,brown_ic))
        except:
            continue
print "Res Similarity is : " + str(res_sim)

#synset1.jcn_similarity(synset2, ic): Jiang-Conrath Similarity Return a score denoting how similar two word senses are, based on the Information Content (IC) of the Least Common Subsumer (most specific ancestor node) and that of the two input Synsets. The relationship is given by the equation 1 / (IC(s1) + IC(s2) - 2 * IC(lcs)
jcn_sim=0
for i in word1:
    for j in word2:
        try:
            jcn_sim=max(jcn_sim,i.jcn_similarity(j,brown_ic))
        except:
            continue
print "JCN Similarity is : " + str(jcn_sim)

#synset1.lin_similarity(synset2, ic): Lin Similarity: Return a score denoting how similar two word senses are, based on the Information Content (IC) of the Least Common Subsumer (most specific ancestor node) and that of the two input Synsets. The relationship is given by the equation 2 * IC(lcs) / (IC(s1) + IC(s2)).
lin_sim=0
for i in word1:
    for j in word2:
        try:
            lin_sim=max(lin_sim,i.lin_similarity(j,brown_ic))
        except:
            continue
print "lin Similarity is : " + str(lin_sim)