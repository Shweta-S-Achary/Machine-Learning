import sys

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

labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
n = []
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


#CALCULATING MEAN: formula (Sum)/(Total number)

m0 = []
for j in range(0, cols, 1):
    m0.append(0.001)

m1 = []
for j in range(0, cols, 1):
    m1.append(0.001)

for i in range(0, rows, 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            m0[j] = m0[j] + data[i][j]
    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(0, cols, 1):
            m1[j] = m1[j] + data[i][j]

for j in range(0, cols, 1):
    m0[j] = m0[j]/n[0]
    m1[j] = m1[j]/n[1]

print("MEAN OF BOTH CLASSES:-")
print(m0)
print(m1)

#CALCULATING VARIANCE: formula Sum of(xi-mean)^2/(total number)

var0 = []
for j in range(0, cols, 1):
    var0.append(0.001)

var1 = []
for j in range(0, cols, 1):
    var1.append(0.001)

for i in range(0, len(trainlabels), 1):
    if(trainlabels.get(i) != None and trainlabels[i] == 0):
        for j in range(0, cols, 1):
            var0[j] = var0[j] + (data[i][j] - m0[j])**2

    if(trainlabels.get(i) != None and trainlabels[i] == 1):
        for j in range(0, cols, 1):
            var1[j] = var1[j] + (data[i][j] - m1[j])**2

#print(var0)
#print(var1)

for j in range(0, cols, 1):
    var0[j] = var0[j]/n[0]
    var1[j] = var1[j]/n[1]

print("VARIANCE OF BOTH CLASSES:-")
print(var0)
print(var1)


#PREDICTING THE CLASS

print("CLASS PREDICTION:-")
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        d0 = 0
        d1 = 0
        for j in range(0, cols, 1):
            d0 = d0 + (data[i][j] - m0[j])**2/var0[j]
            d1 = d1 + (data[i][j] - m1[j])**2/var1[j]
        if(d0<d1):
            print("0",i)
        else:
            print("1",i)         

















