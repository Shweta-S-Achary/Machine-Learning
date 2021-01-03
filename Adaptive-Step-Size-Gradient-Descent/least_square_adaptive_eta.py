import sys
import random
import math


def dP(l, m):
    prod = []
    mul = 0
    for i in range(0, len(l), 1):
        mul += l[i] * m[i]
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


#converting labels from 0 to -1
convtrainlabels = {}
for j in trainlabels:
    if trainlabels[j] == 0:
        convtrainlabels[j] = -1
    else:
        convtrainlabels[j] = trainlabels[j]
#print("CONVERTED TRAIN LABELS:-")
#print(convtrainlabels)


#initializing vector w
w = []
for i in range (0, cols, 1):
    a = random.uniform(-0.01,0.01)
    w.append(a)
#print("Initial W is:-")
#print(w)


#eta = 0.0001
previous_error = 0.0
theta = 0.001
count = 1
error = 0


while(True):
    d = []
    deltaW = []
    dW = 0
    deltaE = []
    

    #computing error
    for i in range(0, rows, 1):
        if(convtrainlabels.get(i) != None):
            error += ((convtrainlabels.get(i) - dP(w, data[i]))**2)
    error = error/2
    #print("Updated error is:-")
    #print(error)

    #checking condition
    if(count > 1):
        if(previous_error - error <= theta):
            #print("*****THRESHOLD CONDITION SATIFIED*****")
            break
  
    for i in range(0, cols, 1):
        deltaE.append(0)
        
    for i in range(0, rows, 1):
        if(convtrainlabels.get(i) != None):
            dp = dP(w, data[i])
            for j in range(0, cols, 1):
                deltaE[j] += ((convtrainlabels.get(i) - dp)*data[i][j])
        #print(z)
        #d.append(z)

    eta_list = [1, .1, .01, .001, .0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001 ]
    bestobj = 1000000000000 # infinity
    previous_err = 0
    eta1 = 0
    best_eta = 0
    obj = 0
    bestobj = 0
    for k in range(0, len(eta_list), 1):
        eta1 = eta_list[k]
             
        for i in range(0, cols, 1):
            w[i] = w[i] + eta1*deltaE[i]

        err = 0
        for i in range(0, rows, 1):
            if(convtrainlabels.get(i) != None):
                err += ((convtrainlabels.get(i) - dP(w, data[i]))**2)
        err = err/2

        obj = err
        
        if(obj < previous_err):
            bestobj = obj
            best_eta = eta1
            
        previous_err = err
        
        for i in range(0, cols, 1):
            w[i] = w[i] - eta1*deltaE[i] 

    eta = best_eta
    #print("ETA USED IS:-->", eta)
    for i in range(0, cols, 1):
        w[i] = w[i] + eta*deltaE[i]

    previous_error = error
    error = 0
    count += 1
    
#print("Updated W is:-")
#print(w)


#hyperplane
w_dash = []
#print("Hyperplane is:-")
'''
for i in range(0, len(w)-1, 1):
    if(w[i+1] != ''):
        w_dash[i] = w[i+1]
print(w_dash)
'''
for i in range(1, len(w), 1):
    w_dash.append(w[i])
#print(w_dash)

dist = [1]
#distance from origin
#print("Distance from origin is:-")
dist = dP(w_dash, w_dash)
distance = abs(w[0]/math.sqrt(dist))
#print(distance)


#prediction of class
#print("CLASS PREDICTION:-")
for i in range(0, rows, 1):
    if(trainlabels.get(i) == None):
        dp = dP(w, data[i])
        #print("Dot product is:-",dp)
        if(dp > 0):
            print("1",i)
        else:
            print("0",i)
        
