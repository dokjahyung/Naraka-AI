import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def construct_matrix(x):
    A_x = np.vstack((x ** 3, x ** 2, x, np.ones_like(x))).T
    return A_x

def coefficient_eq(A_x, y):
    coefficients_x, _, _, _ = np.linalg.lstsq(A_x, y, rcond=None)
    return coefficients_x

def lstSq(A_x, y):
    coefficients_x = coefficient_eq(A_x, y)
    print(f"coefficients: {coefficients_x}")
    predicted_x_y = np.dot(A_x, coefficients_x)
    return predicted_x_y
    

def plot(x, y, predicted_x_y, label_x, label_y, color):
    fig1, ax1 = plt.subplots()
    
    ax1.scatter(x, y, c=color, label='Data points')
    ax1.plot(x, predicted_x_y, color='blue', label='Regression line')
    ax1.set_xlabel(label_x)
    ax1.set_ylabel(label_y)
    ax1.legend()
    
def lstsq_construct(x, y, label_x, label_y, color):
    A_x = construct_matrix(x)
    predicted_x_y = lstSq(A_x, y)
    print(predicted_x_y)
    plot(x, y, predicted_x_y, label_x, label_y, color)
    
def expected_y(coefficients_x, x):
    expect_y = coefficients_x[0]*x**3 + coefficients_x[1]*x**2 + coefficients_x[2]*x + coefficients_x[3]
    return expect_y

def residual(y, expect_y):
    return (y - expect_y)

def residual_total(x, y, coefficients_x):
    r_total = 0
    for point in range(x.size):
        expect_y = expected_y(coefficients_x, x[point])
        r_total += residual(y[point], expect_y)**2
    return r_total

def mean_y(y):
    total = 0
    for value in y:
        total += value
    return total/float(y.size)

def TSS(y):
    total = 0
    mean_y_ = mean_y(y)
    for point in y:
        total += (point - mean_y_)**2
    return total

def r_squared(x, y):
    r_sub_mean_ = TSS(y)
    A_x = construct_matrix(x)
    coefficients_x = coefficient_eq(A_x, y)
    residual_total_ = residual_total(x, y, coefficients_x)
    
    r_squared_ = 1 - (residual_total_/r_sub_mean_)
    return r_squared_