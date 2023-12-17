import function as fn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import prediction as pred
from prediction import avePtsArray, assists, killsAve
import mass_calculate


#pred.prediction_software()


mass_calculate.factorial_rsq(9, avePtsArray, 1)
'''
fn.lstsq_cubic_construct(['1','6'], killsAve, assists, avePtsArray, 'killsAve', 'assists', 'avePtsArray', 'r')
plt.show()
print("")
print("")
print("here is the cubic")
mass_calculate.factorial_rsq(6, avePtsArray, 3)
fn.lstsq_construct(killsAve, avePtsArray, 'killsAve', 'avePtsArray', 'r')
'''