#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Author: Andrea Ceolin
February 2021

This script is adapted from Introduction to Programming in Python (Sedgewick, Wayne and Dondero 2015).
It is used to correlate syntactic and geographic distances.
'''

import math
import sys

'''
This variable keeps track of the subfamilies.
'''

families = {'Hu' : 'ugr', 'Kh': 'ugr',
'Est' : 'fu', 'Fin' : 'fu',
'mM' : 'vol',
'Ud' : 'per',
'Ev1' : 'evk', 'Ev2' : 'evk', 'Ek' : 'evk',
'Ya': 'tur', 'Uz' : 'tur', 'Kaz' : 'tur', 'Kyr': 'tur', 'Tur' : 'tur',
'Bur' : 'bur',
'Sic': "rom", 'NCa': "rom", 'It': "rom", 'Sp': "rom", 'Fr': "rom", 'Ptg': "rom", 'Rm': "rom",
'CG' : "grk", 'Grk': "grk", 'CyG': "grk",
'E': "ger", 'Du' : "ger", 'Afk' : "ger", 'D': "ger", 'Da': "ger", 'Ice': "ger", 'FO': "ger", 'Nor': "ger",
'Blg': "sla", 'SC': "sla", 'Slo': "sla", 'Po': "sla", 'Rus': "sla",
'Ir': "cel", 'Wel': "cel",
'Ma': "indo", 'Hi': "indo", 'Pas': "indo"}


'''
These functions are used to calculate Jaccard distances between two strings of parameters
'''
def jaccard_syn(P1, P2):
    id = 0.0
    dif = 0.0
    for i in range(len(P1)):
        if P1[i] == P2[i] == "+":
            id += 1
        elif (P1[i] == "+" and P2[i] == "-") or (P1[i] == "-" and P2[i] == "+"):
            dif += 1
    dist = dif / (dif + id)
    return dist

def get_syn(parameters):
    syn_list = []
    lang_syn = [line.split()[0] for line in open(parameters, 'r')]
    with open(parameters, 'r') as f:
        pars = f.readlines()
        for index, lang1 in enumerate(pars):
            for lang2 in pars[index+1:]:
                L1 = lang1.split()
                L2 = lang2.split()
                syn_list.append([L1[0]+'-'+L2[0], round(jaccard_syn(L1,L2), 3)])
    return lang_syn, syn_list


'''
These functions are used to calculate Great Circle Distances from a list of coordinates
'''

def gcd(X, Y):
    # Accept float command-line arguments x1, y1, x2, and y2: the latitude
    # and longitude, in degrees, of two points on the earth. Compute and
    # write to standard output the great circle distance (in nautical
    # miles) between those two points.

    # The following formulas assume that angles are expressed in radians.
    # So convert to radians.
    x1, y1 = X
    x2, y2 = Y
    x1 = math.radians(float(x1))
    y1 = math.radians(float(y1))
    x2 = math.radians(float(x2))
    y2 = math.radians(float(y2))
    # Compute using the law of cosines.
    # Great circle distance in radians
    # use rounding to avoid >1 for estimating distance 0
    angle1 = math.acos(round(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2), 5))
    # Convert back to degrees.
    angle1 = math.degrees(angle1)
    # Each degree on a great circle of Earth is 60 nautical miles.
    distance1 = 60.0 * angle1
    return distance1

def get_geo(geo_coord):
    coord_distances = []
    coords = [line.split() for line in open(geo_coord, 'r')]
    coords = coords[1:]
    for index, lang1 in enumerate(coords):
        for index2, lang2 in enumerate(coords[index+1:]):
            coord_distances.append([lang1[0]+'-'+lang2[0], str(gcd(lang1[1:3], lang2[1:3]))])
    return coords, coord_distances


def main(geo_coord, syn_table, outfile):

    lang_syn, syn_list = get_syn(syn_table)
    coords, coord_distances = get_geo(geo_coord)
    print(len(coords))
    print(len(lang_syn))
    print(len(coord_distances))
    print(len(syn_list))

    f = open(outfile, 'w')
    for index, _ in enumerate(syn_list):
        lang1, lang2 = syn_list[index][0].split('-')
        #filter out languages which belong to the same subfamily
        if families[lang1] != families[lang2]:
            f.write('%s\t%s\t%s\t%s\n' %(coord_distances[index][0], syn_list[index][0], coord_distances[index][1], syn_list[index][1]))
    f.close()

if __name__ == "__main__":
    try:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print('ERROR. Use the following arguments: geo_coordinates syntactic_data output_file_name')