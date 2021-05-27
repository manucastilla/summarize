from itertools import chain
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
from nltk.corpus import stopwords
from argparse import ArgumentParser

MSG_DESCRIPTION = "summarize a text"


def LSA_matrix(sents):
    # colocar tudo junto
    words = set(chain.from_iterable(sents))
    word_index = {word: k for k, word in enumerate(words)}
    num_words = len(word_index)
    num_sents = len(sents)
    # Input matrix creation:
    # The cells are used to represent the importance of words in sentences
    X = np.zeros((num_words, num_sents))
    for d, sent in enumerate(sents):
        for word in sent:
            w = word_index[word]
            X[w, d] += 1
    # Singular Value Decomposition:
    # model relationships among words/phrases and sentences
    U, S, Vt = np.linalg.svd(X)  # S os valores da diagonal
    V = Vt.transpose()

    return U, V, S, Vt, num_sents


def cross_method(Vt, k, num_sentences, sents):
    # cross method
    # VT matrix is used for sentence selection purposes
    # pre-processing step is to remove the overall effect of sentences that are related to the concept somehow, but not the core sentence for that concept

    # rows of the VT matrix, the average sentence score is calculated
    vt = np.abs(Vt)
    mean = []
    # k comprimento do sumário
    for c in vt:
        mean.append(np.mean(c))

    # removes less related sentences while keeping more related ones for that concept.
    for i in range(k):
        for j in range(len(vt)):
            if vt[i][j] <= mean[i]:
                vt[i][j] = 0

    # the total length of each sentence vector, which is represented by a column of the VT matrix, is calculated.
    # axis=0:
    total_length = len(vt[0])
    sum_l = vt.sum(axis=0)
    l_score = []

    for i in range(total_length):
        l_score.append([sum_l[i], i])

    # sen1 has the highest length score, so it has been chosen to be part of the summary.
    l_score.sort(reverse=True)
    idx = [i[1] for i in l_score[0:num_sentences]]
    for i in idx:
        print(" ".join(sents[i]))


def main():
    parser = ArgumentParser(description=MSG_DESCRIPTION)
    parser.add_argument('filename_docs', help='Os doc.')
    parser.add_argument('num_sentences', help='number of sentences', type=int)
    parser.add_argument('num_concepts', help='number of concepts', type=int)

    args = parser.parse_args()

    with open(args.filename_docs, "r", encoding="utf-8") as f:
        t = f.read()

    # http://www.nltk.org/api/nltk.tokenize.html?highlight=word_tokenize
    sents = [word_tokenize(i) for i in sent_tokenize(t)]

    U, V, S, Vt, num_sents = LSA_matrix(sents)
    k = args.num_concepts
    cross_method(Vt, k, args.num_sentences, sents)


if __name__ == '__main__':
    main()
