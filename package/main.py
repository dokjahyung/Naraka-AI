import function as fn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import prediction as pred
from prediction import killsAve, endGameKills, avePtsArray, rankPtsAve, healing, damage, assists
import mass_calculate

mass_calculate.factorial_rsq(6, avePtsArray)

pred.prediction_software()
'''
fn.lstsq_construct(killsAve, avePtsArray, 'killsAve', 'avePtsArray', 'r')
'''
