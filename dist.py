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
        #an identity on '+' is counted as an identity
        if P1[i] == P2[i] == "+":
            id += 1
        #differences are counted on the characters that exhibit a '+'/'-' contrast. '?' and '0' are ignored
        elif (P1[i] == "+" and P2[i] == "-") or (P1[i] == "-" and P2[i] == "+"):
            dif += 1
    #return Jaccard distance
    dist = dif / (dif + id)
    return dist


def hamming(P1, P2):
    """Computes the Hamming distance between two strings.

    Args:
        P1: The first string.
        P2: The second string.

    Returns:
        The Hamming distance between the two strings.
    """

    # Check if the strings are the same length
    if len(P1) != len(P2):
        raise ValueError("Strings must be the same length. Hamming extension must be implemented for different string lengths.")

    # Initialize a counter for the number of mismatches
    num_mismatches = 0

    # Iterate over the strings and count the number of mismatches
    # this excludes the 0 items
    for i in range(len(P1)):
        if P1[i] == "+" and P2[i] == "-" or P1[i] == "-" and P2[i] == "+":
            num_mismatches += 1

    normalized_hamming_distance = num_mismatches / len(P1)

    return normalized_hamming_distance

'''
Read a list of languages and features, calculate Hamming distances, and print them in matrix format
'''
def main_hamming(parameters):
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
                dist[L1[0]][L2[0]] = round(hamming(L1,L2), 3)
    #print dictionary in matrix format
    output = open('TableS3_hamming', 'w')
    output.write('\t' + '\t'.join(languages) + '\n')
    for lang in languages:
        output.write(lang + '\t' + '\t'.join([str(dist[lang][lang2]) for lang2 in languages]) + '\n')
    output.close()


'''
Read a list of languages and features, calculate Jaccard distances, and print them in matrix format
'''
def main_jaccard(parameters):
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
    output = open('TableS3', 'w')
    output.write('\t' + '\t'.join(languages) + '\n')
    for lang in languages:
        output.write(lang + '\t' + '\t'.join([str(dist[lang][lang2]) for lang2 in languages]) + '\n')
    output.close()


if __name__ == '__main__':
    main_jaccard(sys.argv[1])
    main_hamming(sys.argv[1])
