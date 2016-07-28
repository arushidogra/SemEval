#Arushi Dogra
'''Same way coding

This measure computes the similarity between
sentences using the semantic alignment of lemmas.
First we compute the word similarity between
all pairs of lemmas from the first and the
second sentence, using either the knowledge-based
or the corpus-based semantic similarity. We then
greedily search for a pair of most similar lemmas;
once the lemmas are paired, they are not considered
for further matching. Previous research by Lavie
and Denkowski (2009) proposed a similar alignment
strategy for machine translation evaluation. After
aligning the sentences, the similarity of each lemma
pair is weighted by the larger information content of
the two lemmas:
    sim(l1, l2) = max(ic(l1), ic(l2))· ssim(l1, l2) (2)
    where ssim(l1, l2) is the semantic similarity between
    lemmas l1 and l2.
    The overall similarity between two sentences is
    defined as the sum of similarities of paired lemmas
    normalized by the length of the longer sentence:
    glao(S1, S2) =
    P
    (l1,l2)∈P
    sim(l1, l2)
    max(length(S1), length(S2))
    where P is the set of lemma pairs obtained by greedy
    alignment. We take advantage of greedy align overlap
    in two features: one computes glao(·, ·) by using
    the Lin similarity for ssim(·, ·) in (2), while the
    other feature uses the distributional (LSA) similarity
    to calculate ssim(·, ·).


'''
