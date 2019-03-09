from sklearn.tree import DecisionTreeClassifier
# 0 for bumpy and 1 for smooth
# label 0 for Apple and 1 for orange
a = [[130, 1], [140, 1], [150, 0], [170, 0]]
label = [0, 0, 1, 1]

clf = DecisionTreeClassifier()
clf = clf.fit(a,label)


print(clf.predict([[160,0]]))
