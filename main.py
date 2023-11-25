import function as fn
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#possible x values
#average kills in 6 set game
killsAve = np.array([9.2, 8.2, 8, 7.4, 7.2, 6.2, 6.2, 5.8, 4.6, 4.4, 4.4, 4.4, 4.2, 3.8])
#placement points
rankPtsAve = np.array([3, 1.8, 1.5, 1.5, 1.9, 1, 1, 0.8, 1.1, 0.8, 0.8, 0.7, 0.7, 0.8])
#this was perhaps the strongest r value in the sets, kills at last 2-5 min of game
endGameKills = np.array([4.3, 2.3, 2.1, 2.6, 1.2, 1, 1.3, 1.3, 1.1, 0.8, 1.5, 0.6, 0.3, 0.4])
#healing had a stronger impact on total points than damage did. this I believe is because of how it means teams with greater survivability
#had great placement points and kill multipliers. Common misconception I found here as a veteran player is that although the game has tried to curb passive gameplay
#The strongest strategy is to be aggressive only in no risk situations and remain passive
healing = np.array([25462.80, 23775.10, 26110.30, 25027.90, 20871.10, 24847.20, 19557.70, 17014.70, 22304.00, 16935.30, 16394.90, 18502.00, 16598.70, 16904.60])
#damage had a strong correlation with total points in excel but this is not useful for a player to determine anything except oppressive skill wins above all
damage = np.array([46735.1, 29678, 33205.9, 34882.6, 28798.1, 29474.8, 33250.6, 25500.6, 27269.9, 27327.4, 27264.4, 27288, 20586.5, 22071.6])
#teams can only have a max of 2x there kills. in excel saw a deep correlation between assists and points. more coordinated teams tend to do well
assists = np.array([13.5, 11.6, 11.5, 9.2, 7.3, 9.4, 9.1, 7.8, 5.6, 6.1, 5, 6, 5.3, 4.5])
#possible y values
#win rate %
winRateCent = np.array([0.2619047619, 0.2023809524, 0.1071428571, 0.1428571429, 0.1388888889,
    0.08333333333, 0.04761904762, 0.05952380952, 0.04166666667, 0.03846153846,
    0.04761904762, 0.04166666667, 0.05, 0, 0, 0, 0, 0.02083333333])
#total points during the 6 game set
TotalPoints = np.array([206.20, 162.10, 157.30, 142.10, 127.70, 127.20, 112.90, 104.70, 90.50, 79.60, 82.20, 79.20, 74.00, 65.80])
#easier way to crunch data if it's an ave
avePtsArray = TotalPoints/6

killsAve_rsq = fn.r_squared(killsAve, avePtsArray)
print(f" killsAve r SQ = {killsAve_rsq}")
healing_rsq = fn.r_squared(healing, avePtsArray)
print(f" healing r SQ = {healing_rsq}")
damage_rsq = fn.r_squared(damage, avePtsArray)
print(f" damage r SQ = {damage_rsq}")
assists_rsq = fn.r_squared(assists, avePtsArray)
print(f" assists r SQ = {assists_rsq}")
endGameKills_rsq = fn.r_squared(endGameKills, avePtsArray)
print(f" endGameKills r SQ = {endGameKills_rsq}")

fn.lstsq_construct(killsAve, avePtsArray, 'killsAve', 'avePtsArray', 'r')
fn.lstsq_construct(healing, avePtsArray, 'healing', 'avePtsArray', 'g')
fn.lstsq_construct(damage, avePtsArray, 'damage', 'avePtsArray', 'b')
fn.lstsq_construct(assists, avePtsArray, 'assists', 'avePtsArray', 'b')
fn.lstsq_construct(endGameKills, avePtsArray, 'endGameKills', 'avePtsArray', 'b')
plt.show()
