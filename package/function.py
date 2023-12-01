import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matrix
'''
def construct_linear_interact_cubic_matrix(x,y):
    A_x = np.vstack((x**3, x**2, x, x*y, y**3, y**2, y, np.ones_like(x))).T
    return A_x

def construct_cubic_matrix(x):
    A_x = np.vstack((x ** 3, x ** 2, x, np.ones_like(x))).T
    return A_x
'''
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

'''
def lstsq_linear_interaction_cubic_construct(x, y, label_x, label_y, color, interact):
    A_x = construct_linear_interact_cubic_matrix(x, interact)
    predicted_x_y = lstSq(A_x, y)
    print(predicted_x_y)
    plot(x, y, predicted_x_y, label_x, label_y, color)
    
def lstsq_cubic_construct(x, y, label_x, label_y, color):
    A_x = construct_cubic_matrix(x)
    predicted_x_y = lstSq(A_x, y)
    print(predicted_x_y)
    plot(x, y, predicted_x_y, label_x, label_y, color)  
    
def expected_linear_interaction_cubic_y(coefficients_x, x, y):
    expect_y = coefficients_x[0]*x**3 + coefficients_x[1]*x**2 + coefficients_x[2]*x + coefficients_x[3]*x*y + coefficients_x[4]*y**3 + coefficients_x[5]*y**2 + coefficients_x[6]*y + coefficients_x[7]
    return expect_y
''' 
def expected_y(coefficients_x, variable_list, point):
    expect_y = matrix.extend_equation(coefficients_x, variable_list, point)
    return expect_y

def residual(y, expect_y):
    return (y - expect_y)

'''
def residual_linear_interaction_total(x, y, coefficients_x, interact):
    r_total = 0
    for point in range(x.size):
        expect_y = expected_y(coefficients_x, x[point], interact[point])
        r_total += residual(y[point], expect_y)**2
    return r_total
'''

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
    print(len(coefficients_x))
    residual_total_ = residual_cubic_total(variable_list, y, coefficients_x)
    
    r_squared_ = 1 - (residual_total_ / r_sub_mean_)
    '''
    if(len(variable_list) == 1):
        return r_squared_
    else:
        r_squared_ = adjusted_r_squared(r_squared_, y.size, len(variable_list))
    '''
    return r_squared_



def adjusted_r_squared(r_squared, n, k):
    adjusted_r_squared = 1 - ((1 - r_squared) * (n - 1) / (n - k - 1))
    return adjusted_r_squared


'''
def r_squared_linear_interact(x, y, interact):
    r_sub_mean_ = TSS(y)
    A_x = construct_linear_interact_cubic_matrix(x, interact)
    coefficients_x = coefficient_eq(A_x, y)
    residual_total_ = residual_linear_interaction_total(x, y, coefficients_x, interact)
    
    r_squared_ = 1 - (residual_total_/r_sub_mean_)
    return r_squared_
'''
