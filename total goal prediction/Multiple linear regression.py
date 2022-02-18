import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv('CSV FILE')
y = data.iloc[:, 8:9].values
x = data.iloc[:, [1,2,4,9,10,11]].values


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
lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)


# # validation
# y_pred = lin_reg.predict(x_val)
# err = mean_squared_error(y_val, y_pred)
# print(err)


# model testing
y_pred = lin_reg.predict(x_test)
err = mean_squared_error(y_test, y_pred)
print(err)
#mean squared error: 2.73
