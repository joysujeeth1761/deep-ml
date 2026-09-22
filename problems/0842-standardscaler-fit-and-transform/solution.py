import numpy as np

def standard_scaler(X_train: np.ndarray, X_test: np.ndarray) -> np.ndarray:
    """
    Fit a standard scaler on X_train and transform X_test.
    Returns the standardized X_test as a numpy array.
    """
    # ypu sould never calculate the mean / var(std) separatly for X_test beacuse it will be a cause for data leakage 

    mean = np.mean(X_train,axis= 0)
    var = np.std(X_train , axis = 0)

    # edge case 
    var[var == 0] = 1.0

    X_test_scaled = (X_test - mean) / var

    return X_test_scaled
