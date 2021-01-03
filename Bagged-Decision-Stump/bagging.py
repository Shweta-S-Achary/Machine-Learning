import sys
import random
import math

#reading data file
datafile = sys.argv[1]
f = open(datafile)
data = []
l = f.readline()
while(l != ''):
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(float(a[j]))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])
f.close()
#print("DATA:-")
#print(data)


#reading labels file
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []   #n[0] is count of -1 labels and n[1] is count of +1 labels
n.append(0)
n.append(0)
l = f.readline()
while(l != ''):
    a = l.split()
    trainlabels[int(a[1])] = int(a[0])
    l = f.readline()
    n[int(a[0])] += 1
        
f.close()
#print("TRAIN LABELS:-")
#print(trainlabels)


def bestsplit(data, labels, col):
    covals = {}
    indices = []
    rows = 0
    minus = 0
    for i in range(0, len(data), 1):
        if(labels.get(i) != None):
            covals[i] = data[i][col]
            indices.append(i)
            rows += 1
            if(labels[i] == 0):
                minus += 1
    sorted_indices = sorted(indices, key=covals.__getitem__)

    lsize = 1
    rsize = rows - 1
    lp = 0
    rp = minus
    if(labels[sorted_indices[0]] == 0):
        lp += 1
        rp -= 1

    bestsplit = -1
    bestgini = 10000
    for i in range(1, len(sorted_indices), 1):
        split = (covals[sorted_indices[i]] + covals[sorted_indices[i-1]])/2
        gini = (lsize/rows)*(lp/lsize)*(1 - lp/lsize) + (rsize/rows)*(rp/rsize)*(1 - rp/rsize)
        if(gini < bestgini):
            bestgini = gini
            bestsplit = split
        if(labels[sorted_indices[i]] == 0):
            lp += 1
            rp -= 1
        lsize += 1
        rsize -= 1

    return(bestsplit, bestgini)



boots = 100
predval = {}
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        predval[i] = 0

for k in range(0, boots, 1):
    i = 0
    bdata = []
    btrainlabels = {}
    while(i < len(data)):
        r = random.randint(0, rows-1)
        if(trainlabels.get(r) != None):
            bdata.append(data[r])
            btrainlabels[i] = trainlabels[r]
            i += 1

    best_split = -1
    best_col = -1
    best_gini = 100000
    for j in range(0, cols, 1):
        [split, gini] = bestsplit(bdata, btrainlabels, j)
        #print(split, gini)
        if(gini < best_gini):
            best_gini = gini
            best_split = split
            best_col = j
            #print(best_col)
    u = 0
    v = 0
    for i in range(0, rows, 1):
        if(trainlabels.get(i) != None):
            if(data[i][best_col] < best_split):
                if(trainlabels[i] == 0):
                    u += 1
                else:
                    v += 1
    if(u > v):
        left = -1
        right = 1
    else:
        left = 1
        right = -1

    for i in range(0, rows, 1):
        if(trainlabels.get(i) == None):
            if(data[i][best_col] < best_split):
                predval[i] += left
            else:
                predval[i] += right

print("CLASS PREDICTION:-")
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        if(predval[i] > 0):
            print("1 ", i)
        else:
            print("0 ", i)
