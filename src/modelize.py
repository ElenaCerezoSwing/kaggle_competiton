from sklearn.linear_model import LinearRegression, Ridge, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor


def get_svm_regression(features):
    from sklearn.svm import LinearSVR
    from sklearn.datasets import make_regression
    X, y = make_regression(n_features=features, random_state=42)
    regr = LinearSVR(random_state=42, tol=1e-5)
    regr.fit(X, y) 


def get_linear_regression_model(X, y, test):
    regressor = LinearRegression()
    regressor.fit(X, y)
    y_pred = regressor.predict(test)
    return y_pred
 
def get_k_neighbors_model(X, y, test):
    neigh = KNeighborsRegressor(n_neighbors=2)
    neigh.fit(X, y) 
    y_pred = neigh.predict(test)
    return y_pred

def get_ridge_model(X, y, test):
    reg = Ridge(alpha=.5, random_state=42)
    reg.fit(X, y)
    y_pred = reg.predict(test)
    return y_pred

def get_sgd_model(X, y, test):
    sgd = SGDRegressor(max_iter=1000, tol=1e-3)
    sgd.fit(X, y)
    y_pred = sgd.predict(test)
    return y_pred



