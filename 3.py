import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test_idx = [0,50,100]

# training data  
#input
train_target = np.delete(iris.target, test_idx)
#output 
train_data = np.delete(iris.data, test_idx, axis = 0)

# test data
#input
test_target = iris.target[test_idx]
#output
test_data = iris.data[test_idx]

# get the classifier and classify the data
# fit is find pattrens in data
clf =tree.DecisionTreeClassifier()
clf = clf.fit(train_data,train_target)

print test_target
print clf.predict(test_data)