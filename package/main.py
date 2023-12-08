import function as fn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import prediction as pred
from prediction import avePtsArray
import mass_calculate

mass_calculate.factorial_rsq(6, avePtsArray, 1)
print("")
print("")
print("here is the cubic")
mass_calculate.factorial_rsq(6, avePtsArray, 3)
#pred.prediction_software()
'''
fn.lstsq_construct(killsAve, avePtsArray, 'killsAve', 'avePtsArray', 'r')
'''