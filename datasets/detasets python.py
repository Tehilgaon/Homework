# -*- coding: utf-8 -*-

'''TEHILA GAON 315136952'''

"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import tree

from sklearn.model_selection import cross_val_score

import matplotlib.pyplot as plt

from sklearn import datasets

from sklearn.metrics import recall_score


# import some data to play with

def calculate(resource, dsName):
    ds = resource

    mylist = []
    # do loop

    clf = tree.DecisionTreeClassifier()

    clf.max_depth = 10

    clf.criterion = 'entropy'

    clf = clf.fit(ds.data, ds.target)

    print("Decision Tree: ")

    accuracy = cross_val_score(clf, ds.data, ds.target, scoring='accuracy', cv=10)

    print("Average Accuracy of  DT with depth ", clf.max_depth, " is: ", round(accuracy.mean(), 3))

    mylist.append(accuracy.mean())  # loop, can be used to plot later…

    precision = cross_val_score(clf, ds.data, ds.target, scoring='precision_weighted', cv=10)

    print("Average precision_weighted of  DT with depth ", clf.max_depth, " is: ", round(precision.mean(), 3))

    recall = cross_val_score(clf, ds.data, ds.target, cv=10, scoring='recall_weighted')

    print("Average recall_weighted of  DT with depth ", clf.max_depth, " is: ", round(recall.mean(), 3))

    f1score = cross_val_score(clf, ds.data, ds.target, cv=10, scoring='f1_weighted')

    print("Average f1score_weighted of  DT with depth ", clf.max_depth, " is: ", round(f1score.mean(), 3))

    X = range(0, 10)
    plt.plot(X, [accuracy[x] for x in X])
    plt.plot(X, [precision[x] for x in X])
    plt.plot(X, [recall[x] for x in X])
    plt.plot(X, [f1score[x] for x in X])
    plt.xlabel(dsName)
    plt.legend(['accuracy', 'precision', 'recall', 'f1score'])
    plt.show()


calculate(datasets.load_iris(), "iris values")
print("The tree depth with the highest accuracy for Iris dataset is 10")

calculate(datasets.load_wine(), "wine values")
print("The tree depth with the highest accuracy for Wine dataset is 7")

calculate(datasets.load_digits(), "digit values")
print("The tree depth with the highest accuracy for Digit dataset is 10")























