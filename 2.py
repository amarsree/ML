# importing data set from package sklearn
from sklearn.datasets import load_iris

# from sklearn import tree
# labling the imported data set
iris = load_iris()



# displays the names
# feature_names =  input  attributes as input
# target_names = outcome , conclution
print iris.feature_names
print iris.target_names

#prints data in that index
print iris.data[0]
print iris.target[0]


print iris.feature_names 
# itrate through data
for i in range(len(iris.target)):
	print iris.data[i],iris.target[i]

#test_idx = [0,50,100]
#training data
#train_target = iris.target[test_idx]
#train_data = iris.data[test_idx]
