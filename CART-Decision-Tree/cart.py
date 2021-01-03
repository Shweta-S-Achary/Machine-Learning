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


list_gini = []
split = 0
templ = [0, 0]
for j in range(0, cols, 1):
    list_gini.append(templ)
temp = 0
column = 0

for j in range(0, cols, 1):

    sortedCol = [item[j] for item in data]
    keys = sorted(range(len(sortedCol)), key=lambda k: sortedCol[k])
    sortedCol.sort()
    #print("Sorted Column",listcolumn)
    #print("Keys",keys)
    gini_val = []
    previous_gini = 0
    #previous_row = 0
    for k in range(1, rows, 1):

        lsize = k
        rsize = rows - k
        lp = 0
        rp = 0

        for u in range(0, k, 1):
            if (trainlabels.get(keys[u]) == 0):
                lp += 1
        for v in range(k, rows, 1):
            if (trainlabels.get(keys[v]) == 0):
                rp += 1
        gini = (lsize / rows) * (lp / lsize) * (1 - lp / lsize) + (rsize / rows) * (rp / rsize) * (1 - rp / rsize)
        gini_val.append(gini)
        #print(gini)
        previous_gini = min(gini_val)
        if (gini_val[k - 1] == float(previous_gini)):
            list_gini[j][0] = gini_val[k - 1]
            list_gini[j][1] = k
    if (j == 0):
        temp = list_gini[j][0]
    if (list_gini[j][0] <= temp):
        temp = list_gini[j][0]
        column = j
        split = list_gini[j][1]
        if (split != 0):
            split = (sortedCol[split] + sortedCol[split - 1]) / 2

print("Column: ", column, "  Gini: ", temp, "  Split: ", split)
