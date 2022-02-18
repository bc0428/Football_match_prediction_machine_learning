import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

data = pd.read_csv('CSV FILE')
y = data.iloc[:, 5:6].values
x = data.iloc[:, [1,2,3,4]].values


# label encoder
le = LabelEncoder()
y = le.fit_transform(y)


# split data
# train:test:val = 6:2:2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state = 0)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size = 0.5, random_state = 0)


# standardise
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
x_val = sc.transform(x_val)


# # validation
# accuracy = []
# for i in range(10,20):
#     # KNN train
#     classifier = KNeighborsClassifier(n_neighbors=i, metric='minkowski', p=2)
#     classifier.fit(x_train, y_train)
#
#     y_pred = classifier.predict(x_val)
#     acc = '%.2f' % accuracy_score(y_val, y_pred)
#     accuracy.append(acc)
#     cm = confusion_matrix(y_val, y_pred)
#     print(cm)

# # k=15 was found to have highest accuracy
# print(accuracy)


# testing
classifier = KNeighborsClassifier(n_neighbors=15, metric='minkowski', p=2)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
acc = '%.2f' % accuracy_score(y_test, y_pred)
# accuracy = 0.53
print(acc)
