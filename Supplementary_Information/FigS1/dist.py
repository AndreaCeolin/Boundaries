#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Andrea Ceolin
November 2019
'''
from collections import defaultdict
import sys

'''
Compute jaccard distances
'''
def jaccard(P1, P2):
    id = 0.0
    dif = 0.0
    for i in range(len(P1)):
        #an identity on '1' is counted as an identity
        if P1[i] == P2[i] == "+":
            id += 1
        #differences are counted on the characters that exhibit a '1'/'0' contrast. '?' are ignored
        elif (P1[i] == "+" and P2[i] == "-") or (P1[i] == "-" and P2[i] == "+"):
            dif += 1
    #return Jaccard distance
    dist = dif / (dif + id)
    return dist

'''
Read a list of languages and features, calculate Jaccard distances, and print them in matrix format
'''
def main(parameters):
    #store the name of each language, which is the first element of each line
    languages = [line.split()[0] for line in open(parameters, 'r')]
    with open(parameters, 'r') as f:
        pars = f.readlines()
        dist = defaultdict(dict)
        #store the pairwise distances in a dictionary
        for lang1 in pars:
            for lang2 in pars:
                L1 = lang1.split()
                L2 = lang2.split()
                dist[L1[0]][L2[0]] = round(jaccard(L1,L2), 3)
    #print dictionary in matrix format
    output = open('jaccard_distances.txt', 'w')
    output.write('\t' + '\t'.join(languages) + '\n')
    for lang in languages:
        output.write(lang + '\t' + '\t'.join([str(dist[lang][lang2]) for lang2 in languages]) + '\n')
    output.close()


if __name__ == '__main__':
    main(sys.argv[1])
