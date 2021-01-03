import sys 
import random
import math


def dP(l, m):
    prod = []
    mul = 0
    for i in range(0, len(l), 1):
        mul += l[i] * m[i]
    #prod.append(mul)
    return mul

#reading data file
datafile = sys.argv[1]
f = open(datafile)
data = []
l = f.readline()
while(l != ''):
    a = l.split()
    l2 = [1.0]
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

#initializing vector w
w = []
for i in range (0, cols, 1):
    a = random.uniform(-0.01,0.01)
    w.append(a)
print("Initial W is:-")
print(w)

eta = 0.001
error = 0
stop_con = 1
count = 0
theta = 0.0000001

for i in range(0, rows, 1):
    if (trainlabels.get(i) != None):
        dp = dP(w, data[i])
        y = 1/(1 + math.exp(-1 * dp))
        error += (-trainlabels.get(i) * math.log(y))-((1- trainlabels.get(i)) * math.log(y * (math.exp(-1 * dp))))

prev_error = error

while(abs(stop_con)>theta): 
	deltaW = []
	for j in range(0,cols,1):
	    deltaW.append(0)

	stop_con = 0
	for i in range(0, rows, 1):
            if (trainlabels.get(i) != None):
                dp = dP(w, data[i])
                y = 1/(1 + math.exp(-1 * dp))
                for j in range(0,cols,1):
                    deltaW[j] += ((trainlabels.get(i)-(y)) * data[i][j])

	for j in range(0, cols, 1):
		w[j] += eta * deltaW[j]

	error = 0
	for i in range(0,rows,1):
            if trainlabels.get(i)!=None:
                dp = dP(w, data[i])
                y = 1/(1+math.exp(-1 * dp))
                error += (-trainlabels.get(i) * math.log(y))-((1-trainlabels.get(i)) * math.log(y*(math.exp(-1 * dp))))	

	count += 1
	print ("error is = ",error)
	stop_con = error - prev_error
	prev_error = error


#hyperplane
w_dash = []
print("Hyperplane is:-")
'''
for i in range(0, len(w)-1, 1):
    if(w[i+1] != ''):
        w_dash[i] = w[i+1]
print(w_dash)
'''
for i in range(1, len(w), 1):
    w_dash.append(w[i])
print(w_dash)

dist = [1]
#distance from origin
print("Distance from origin is:-")
dist = dP(w_dash, w_dash)
distance = abs(w[0]/math.sqrt(dist))
print(distance)


#prediction of class
#print("CLASS PREDICTION:-")
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        dp = dP(w, data[i])
        #print("Dot product is:-",dp)
        if(dp > 0):
            print("Prediction is 1 for ",i)
        else:
            print("Prediction is 0 for ",i)
        




