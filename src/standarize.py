from sklearn.preprocessing import StandardScaler
import pandas as pd

def get_standard_scaler(X, X_test):
    scaler = StandardScaler()
    scaler.fit(X)
    scaler.mean_
    X_transform = pd.DataFrame(scaler.transform(X))
    X_test_transform = pd.DataFrame(scaler.transform(X_test))
    return X_transform, X_test_transform