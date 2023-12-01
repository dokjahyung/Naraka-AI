import function as fn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import prediction as pred
from prediction import killsAve, endGameKills, avePtsArray, rankPtsAve, healing, damage, assists


killsAve_interact_rankPtsAve_rsq = fn.r_squared_linear_interact(killsAve, avePtsArray, rankPtsAve)
print(f" killsAve further interacted with rankPtsAve r_SQ = {killsAve_interact_rankPtsAve_rsq}")
endGameKills_interact_healing_rsq = fn.r_squared_linear_interact(endGameKills, avePtsArray, healing)
print(f" end game kills interacted w/ healing r_SQ = {endGameKills_interact_healing_rsq}")
damage_interact_healing_rsq = fn.r_squared_linear_interact(healing, avePtsArray, damage)
print(f" damage interacted w/ healing r_SQ = {damage_interact_healing_rsq}")
rankPtsAve_interact_healing_rsq = fn.r_squared_linear_interact(rankPtsAve, avePtsArray, healing)
print(f" rank pts interacted w/ healing r_SQ = {rankPtsAve_interact_healing_rsq}")

killsAve_cubic_rsq = fn.r_squared_cubic(killsAve, avePtsArray)
print(f" killsAve r SQ = {killsAve_cubic_rsq}")
rankPtsAve_cubic_rsq = fn.r_squared_cubic(rankPtsAve, avePtsArray)
print(f"rank Points r SQ = {rankPtsAve_cubic_rsq}")
healing_cubic_rsq = fn.r_squared_cubic(healing, avePtsArray)
print(f" healing r SQ = {healing_cubic_rsq}")
damage_cubic_rsq = fn.r_squared_cubic(damage, avePtsArray)
print(f" damage r SQ = {damage_cubic_rsq}")
assists_cubic_rsq = fn.r_squared_cubic(assists, avePtsArray)
print(f" assists r SQ = {assists_cubic_rsq}")
endGameKills_cubic_rsq = fn.r_squared_cubic(endGameKills, avePtsArray)
print(f" endGameKills r SQ = {endGameKills_cubic_rsq}")

pred.predict_y_for_single_input()
'''
fn.lstsq_construct(killsAve, avePtsArray, 'killsAve', 'avePtsArray', 'r')
fn.lstsq_construct(rankPtsAve, avePtsArray, 'endGameKills', 'avePtsArray', 'b')
fn.lstsq_construct(healing, avePtsArray, 'healing', 'avePtsArray', 'g')
fn.lstsq_construct(damage, avePtsArray, 'damage', 'avePtsArray', 'b')
fn.lstsq_construct(assists, avePtsArray, 'assists', 'avePtsArray', 'b')
fn.lstsq_construct(endGameKills, avePtsArray, 'endGameKills', 'avePtsArray', 'b')

plt.show()
'''