# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 22:06:10 2018

@author: Balasubramaniam
"""

# Load libraries
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn import tree
import pydotplus
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Create decision tree classifer object
clf = DecisionTreeClassifier(random_state=0)

# Train model
model = clf.fit(X, y)
# Create DOT data
dot_data = tree.export_graphviz(clf, out_file=None, 
                                feature_names=iris.feature_names,  
                                class_names=iris.target_names)

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_pdf("iris.pdf")


wine = datasets.load_wine()
clf = tree.DecisionTreeClassifier() # init the tree
clf = clf.fit(wine.data, wine.target) # train the tree
# export the learned decision tree
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=wine.feature_names,
                         class_names=wine.target_names,
                         filled=True, rounded=True,
                         special_characters=True)

# Draw graph
graph = pydotplus.graph_from_dot_data(dot_data)

graph.write_pdf("wine.pdf")

from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import label_binarize

n_classes = 3
train_x, test_x, train_y, test_y =train_test_split(wine.data, wine.target,
                                                   test_size=0.2, random_state=666)
# binarize class labels to plot ROC
train_y = label_binarize(train_y, classes=[0, 1, 2])
test_y = label_binarize(test_y, classes=[0, 1, 2])

y_score = clf.fit(train_x, train_y).predict(test_x)

print(y_score)

fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(test_y[:, i], y_score[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(test_y.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

#ROC curve for a specific class here for all classes
print(roc_auc)
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
fpr["micro"], tpr["micro"], _ = roc_curve(test_y.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])
import matplotlib.pyplot as plt 
plt.figure()
plt.plot(fpr["micro"], tpr["micro"], label='Decision Tree (area = %0.2f)' % roc_auc["micro"])
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.savefig('Log_ROC')
plt.show()