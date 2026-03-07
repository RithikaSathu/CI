from sklearn.linear_model import LinearRegression
import numpy as np

def train_model():
    
    # sample dataset
    X = np.array([[1],[2],[3],[4],[5]])
    y = np.array([2,4,6,8,10])

    model = LinearRegression()
    model.fit(X,y)

    return model


def predict(model,value):
    value = np.array([[value]])
    return model.predict(value)[0]