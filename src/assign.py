from sklearn.model_selection import train_test_split

def assign_X_y(df):
    y = df['price']
    X = df.drop('price',axis=1)
    return X, y

def get_splitted_train_test(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=5)
    return X_train, X_test, y_train, y_test

def assign_y_to_submitted(y_pred):
    sub['price'] = y_pred
    return sub