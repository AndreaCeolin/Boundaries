
import math

# Accept float command-line arguments x1, y1, x2, and y2: the latitude
# and longitude, in degrees, of two points on the earth. Compute and
# write to standard output the great circle distance (in nautical
# miles) between those two points.


def gcd(X, Y):
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

coords = [line.split() for line in open('coord.txt', 'r')]
coords = coords[1:]

rows = []
for index, lang1 in enumerate(coords):
    list = []
    list.append(lang1[0])
    for index2, lang2 in enumerate(coords):
        list.append(str(gcd(lang1[1:3], lang2[1:3])))
    rows.append(list)

f = open('gcd.txt', 'w')
f.write('\t' + '\t'.join([lang[0] for lang in coords]) + '\n')
for row in rows:
    f.write('\t'.join(row) + '\n')
f.close()