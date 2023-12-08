import numpy as np
from prediction import killsAve, endGameKills, avePtsArray, rankPtsAve, healing, damage, assists
import function as fn

data_dict = {
    '1' : killsAve,
    '2' : endGameKills,
    '3' : rankPtsAve,
    '4' : damage,
    '5' : healing,
    '6' : assists 
}

def discern_var(var):
    if data_dict.get(var) is not None:
        attribute = data_dict.get(var)
        return attribute
    else:
        return None

#regardless of amount of values we are testing with we can test correlations with each other
#so the more data you provide the more accurate it becomes
#however it can suffice with even just one
def linear_form(variable_list):
    A_x = np.vstack([np.ones_like(avePtsArray)])
    for point in range(len(variable_list) - 1, -1, -1):
        x = discern_var(variable_list[point])
        stacked_x = np.vstack([x])
        A_x = np.vstack([stacked_x, A_x])
    return A_x.T

def cubic_form(variable_list):
    A_x = np.vstack([np.ones_like(avePtsArray)])
    for point in range(len(variable_list) - 1, -1, -1):
        x = discern_var(variable_list[point])
        stacked_x = np.vstack([x**3, x**2, x])
        A_x = np.vstack([stacked_x, A_x])
    return A_x.T


def extend_equation(coefficients_x, variable_list, point, degree):
    equation = 0
    num_terms_per_var = degree  # Cubic equation: cubic, quadratic, linear
    
    for j in range(len(variable_list)):
        x = discern_var(variable_list[j])
        x = x[point]
        # Assuming the coefficients are ordered from the highest degree to the constant term
        for i in range(num_terms_per_var):
            equation += coefficients_x[i+j*num_terms_per_var] * (x ** (num_terms_per_var - i))
    
    equation += coefficients_x[-1]  # Adding the constant term
    return equation

def extend_predict(coefficients_x, variables, degree):
    equation = 0
    num_terms_per_var = degree
    
    for j in range(len(variables)):
        x = variables[j]
        # Assuming the coefficients are ordered from the highest degree to the constant term
        for i in range(num_terms_per_var):
            equation += coefficients_x[i+j*num_terms_per_var] * (x ** (num_terms_per_var - i))
    
    equation += coefficients_x[-1]
    return equation# Adding the constant term

