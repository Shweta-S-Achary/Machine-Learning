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


#converting labels from 0 to -1
convtrainlabels = {}

#for i in range (0, len(trainlabels), 1):
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


#eta = 0.001
previous_error = 0.0
theta = 0.001
error = 0
v = 0
while(True):
    wdash = []

    for i in range(0, cols, 1):
        wdash.append(0)
    
    #computing w'
    for i in range(0, rows, 1):
        if(convtrainlabels.get(i) != None):
            u = dP(w, data[i])
            v = convtrainlabels.get(i) * u
            for j in range(0,  cols, 1):
                if(v < 1):
                    wdash[j] += -1 * (convtrainlabels.get(i)*data[i][j])
                else:
                    wdash[j] += 0

                    
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
            w[i] = w[i] - eta1*wdash[i]

        err = 0
        for i in range(0, rows, 1):
            if(convtrainlabels.get(i) != None):
                p = dP(w, data[i])
                err += max(0, 1-convtrainlabels.get(i) * p)

        obj = err
        
        if(obj < previous_err):
            bestobj = obj
            best_eta = eta1
            
        previous_err = err
        
        for i in range(0, cols, 1):
            w[i] = w[i] + eta1*wdash[i] 

    eta = best_eta
    #print("ETA USED IS:-->", eta)
    
    #updating w
    for i in range(0, cols, 1):
        w[i] = w[i] - eta*wdash[i]

    error = 0            
    for i in range(0, rows, 1):
        if(convtrainlabels.get(i) != None):
            p = dP(w, data[i])
            error += max(0, 1-convtrainlabels.get(i) * p)
    #print("Error is:- ", error)


    #checking condition
    #if(count > 1):
    if(abs(previous_error - error) <= theta):
        #print("*****THRESHOLD CONDITION SATIFIED*****")
        break                
           

    previous_error = error
    
#print("Updated W is:-")
#print(w)
  
    
#hyperplane
w_dash = []
#print("Hyperplane is:-")
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
    if(convtrainlabels.get(i) == None):
        dp = dP(w, data[i])
        #print("Dot product is:-",dp)
        if(dp > 0):
            print("1",i)
        else:
            print("0",i)
        
