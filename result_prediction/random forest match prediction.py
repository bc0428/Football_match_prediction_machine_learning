import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv('CSV FILE')
y = data.iloc[:, 5:6].values
x = data.iloc[:, [1,2,3,4,9,10,11]].values


# label encoder
le = LabelEncoder()
y = le.fit_transform(y)


# split data
# train:test:val = 6:2:2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.4, random_state=0)
x_test, x_val, y_test, y_val = train_test_split(x_test, y_test, test_size = 0.5, random_state=0)


# standardise
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
x_val = sc.transform(x_val)


# model training
classifier = RandomForestClassifier(n_estimators = 500, criterion = 'entropy', random_state=0)
classifier.fit(x_train, y_train)

# # validation
# y_pred = classifier.predict(x_val)
# cm = confusion_matrix(y_val, y_pred)
# print(cm)
# acc = accuracy_score(y_val, y_pred)
# print(acc)


# model testing
y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
acc = accuracy_score(y_test, y_pred)
print(acc)
#accuracy: 0.477
