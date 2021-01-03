# Bagged-Decision-Stump

This program performs bagging on the decision stump. The input is the data file and labels. The output is the prediction of test datapoints.

The program will create a bootstrapped dataset and then run the decision stump on it and obtain predictions labels. 
It will repeat this a 100 times and output the majority vote of the predictions.

# Command for Execution

python bagging.py ionosphere.data ionosphere.trainlabels.0
