#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'isSimilar' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING_ARRAY sentence_1
#  2. STRING_ARRAY sentence_2
#  3. 2D_STRING_ARRAY similarity_matrix
#

#approach :
# union find ds for list of word pairs.
# then find each word in linear order has same connectivity

#   abc:def ghi:xyz xyz:tba
#   abc : 1
#   def : 2
#   xyz : 3
#   tba : 4
#   ghi : 5

#   1 connected to 2, 5 connected to 3, 3 connected to 4

class unionfind:
    def __init__(self):
        self.words = {}
        self.word_count = 0
        self.mapping = None
        pass

    def add_word (self,w):
        if w in self.words:
            return
        self.words[w] = self.word_count
        self.word_count += 1

    def ready(self):
        # each x is connected with itself. i.e amazing is similar to amazing :)
        self.mapping = [x for x in range(self.word_count)]

    def root(self,u):
        pass

    def connected(self,u,v):
        p = self.words[u]
        q = self.words[v]
        return self.mapping[p] == self.mapping[q]


    def print(self):
        print (f'Number of words : {self.word_count}')
        for k in self.words.keys():
            print (f'{k} : {self.words[k]}')
        print ('mapping')
        for i in range(len(self.mapping)):
            print (f'{i} : {self.mapping[i]}')



    def union(self,u,v):
        p = self.words[u]
        q = self.words[v]
        if q < p:
            p,q = q,p
        # associate p and q are related.
        # approach quick find - for each entry element related to q , mark as p.
        for i in range(len(self.mapping)):
            if self.mapping[i]==q:
                self.mapping[i] = self.mapping[p]


def isSimilar(sentence_1, sentence_2, similarity_matrix):
    if not len(sentence_1) == len(sentence_2):
        return False
    uf = unionfind()
    for i in range(len(similarity_matrix)):
        uf.add_word(similarity_matrix[i][0])
        uf.add_word(similarity_matrix[i][1])
    uf.ready()
    for i in range(len(similarity_matrix)):
        u = similarity_matrix[i][0]
        v = similarity_matrix[i][1]
        uf.union(u,v)
    similar = True

    for i in range(len(sentence_1)):
        p = sentence_1[i]
        q = sentence_2[i]
        if not uf.connected(p,q):
            similar = False
            break
    return similar
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence_1_count = int(input().strip())

    sentence_1 = []

    for _ in range(sentence_1_count):
        sentence_1_item = input()
        sentence_1.append(sentence_1_item)

    sentence_2_count = int(input().strip())

    sentence_2 = []

    for _ in range(sentence_2_count):
        sentence_2_item = input()
        sentence_2.append(sentence_2_item)

    similarity_matrix_rows = int(input().strip())
    similarity_matrix_columns = int(input().strip())

    similarity_matrix = []

    for _ in range(similarity_matrix_rows):
        similarity_matrix.append(input().rstrip().split())

    result = isSimilar(sentence_1, sentence_2, similarity_matrix)

    fptr.write(str(int(result)) + '\n')

    fptr.close()


#

# 3
# amazing
# acting
# abilities
# 3
# fine
# theatrics
# talent
# 4
# 2
# amazing fine
# fine good
# acting theatrics
# abilities talent
