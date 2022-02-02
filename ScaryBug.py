from sklearn import tree


# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# create a classifier and train it

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

height = int(input("how tall are you (cm)?:"))
weight = int(input("what´s your weight(kg)?:"))
shoe_size = int(input("What´s your shoe number?:"))

prediction = clf.predict([[height,weight,shoe_size]])

print (prediction)
