import sys
from sklearn.svm import LinearSVC
import random

###Reading Data from file

def dot_product(w1,d):
	dp1=0
	for j in range(0,cols,1):
		dp1= dp1 + (w1[j]*d[j])
	return dp1

new_data=[]
k_in=int(sys.argv[3])
datafile=sys.argv[1]
f=open(datafile)
data=[]
datax=[]
line=f.readline()
while(line !=''):
	row=line.split( )
	rowf=[]
	for i in range(0,len(row),1):
		rowf.append(float(row[i]))
	data.append(rowf)
	rowf.append(1)
	datax.append(rowf)
	line=f.readline()
num_rows=len(data)
cols=len(data[0])
f.close()

###Reading Labels from file

label_file=sys.argv[2]
f=open(label_file)
train_labels={}
line=f.readline()
num=[0,0]
while(line!=''):
	row=line.split( )
	train_labels[int(row[1])]=int(row[0])
	if int(row[0])==0:
		train_labels[int(row[1])]=-1
	line=f.readline()
	num[int(row[0])]+=1

test=[]
train=[]
train_new=[]
test_new=[]
trainlabels=[]
for i in range(0,num_rows,1):
	if train_labels.get(i)==None:
		test.append(data[i])
	else:
		train.append(data[i])
		if train_labels.get(i)==-1:
			trainlabels.append(0)
		else:	
			trainlabels.append(1)

for i in range(0,num_rows,1):
	new_data.append([])
	
clf = LinearSVC(max_iter=10000)
clf.fit(train, trainlabels)
predictions = clf.predict(test)
j=0
for i in range(0,num_rows,1):
	if train_labels.get(i)==None:
		#print(predictions[j],i)
		j=j+1
		
for i in range(0,k_in,1):
	w=[]
	for j in range(0,cols,1):
		w.append(random.uniform(1,-1))
	min=1000000000
	max=0
	for k in range(0,num_rows,1):
		dp=dot_product(w,data[k])
		if dp>max:
			max=dp
		if dp<min:
			min=dp
	w0=random.uniform(max,min)
	w.append(w0)
	for k in range(0,num_rows,1):
		dp=dot_product(w,datax[k])
		if dp<0:
			new_data[k].append(0)
		else:
			new_data[k].append(1)
for i in range(0,num_rows,1):
	if train_labels.get(i)==None:
		test_new.append(new_data[i])
	else:
		train_new.append(new_data[i])
clf = LinearSVC(max_iter=10000)
clf.fit(train_new, trainlabels)
predictions = clf.predict(test_new)
j=0
for i in range(0,num_rows,1):
	if train_labels.get(i)==None:
		print(predictions[j],i)
		j=j+1

