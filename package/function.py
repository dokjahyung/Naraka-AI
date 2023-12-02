import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matrix

def coefficient_eq(A_x, y):
    coefficients_x = np.linalg.inv(A_x.T @ A_x) @ A_x.T @ y
    #coefficients_x, _, _, _ = np.linalg.lstsq(A_x, y, rcond=None)
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
    
def lstsq_cubic_construct(variable_list, x, y, label_x, label_y, color):
    A_x = matrix.cubic_form(variable_list)
    predicted_x_y = lstSq(A_x, y)
    print(predicted_x_y)
    plot(x, y, predicted_x_y, label_x, label_y, color)

def expected_y(coefficients_x, variable_list, point):
    expect_y = matrix.extend_equation(coefficients_x, variable_list, point)
    return expect_y

def residual(y, expect_y):
    return (y - expect_y)

def residual_cubic_total(variable_list, y, coefficients_x):
    r_total = 0
    num_points = y.size
    
    for point in range(num_points):
        expect_y = expected_y(coefficients_x, variable_list, point)
        r_total += residual(y[point], expect_y) ** 2
    
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

def r_squared_cubic(variable_list, y):
    r_sub_mean_ = TSS(y)
    A_x = matrix.cubic_form(variable_list)
    coefficients_x = coefficient_eq(A_x, y)
    residual_total_ = residual_cubic_total(variable_list, y, coefficients_x)
    
    r_squared_ = 1 - (residual_total_ / r_sub_mean_)
    return r_squared_


def present_cubic_rsq(variable_list, text, y):
    cubic_rsq = r_squared_cubic(variable_list, y)
    print(f" {text} r_SQ = {cubic_rsq}")