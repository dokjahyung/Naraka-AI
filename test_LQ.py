import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the x and z values
killsAve = np.array([9.2, 8.2, 8, 7.4, 7.2, 6.2, 6.2, 5.8, 4.6, 4.4, 4.4, 4.4, 4.2, 3.8])
rankPtsAve = np.array([3, 1.8, 1.5, 1.5, 1.9, 1, 1, 0.8, 1.1, 0.8, 0.8, 0.7, 0.7, 0.8])
TotalPoints = np.array([206.20, 162.10, 157.30, 142.10, 127.70, 127.20, 112.90, 104.70, 90.50, 79.60, 82.20, 79.20, 74.00, 65.80])
avePtsArray = TotalPoints/6
endGameKills = np.array([4.3, 2.3, 2.1, 2.6, 1.2, 1, 1.3, 1.3, 1.1, 0.8, 1.5, 0.6, 0.3, 0.4])
healing = np.array([25462.80, 23775.10, 26110.30, 25027.90, 20871.10, 24847.20, 19557.70, 17014.70, 22304.00, 16935.30, 16394.90, 18502.00, 16598.70, 16904.60])
damage = np.array([46735.1, 29678, 33205.9, 34882.6, 28798.1, 29474.8, 33250.6, 25500.6, 27269.9, 27327.4, 27264.4, 27288, 20586.5, 22071.6])
assists = np.array([13.5, 11.6, 11.5, 9.2, 7.3, 9.4, 9.1, 7.8, 5.6, 6.1, 5, 6, 5.3, 4.5])
# Define the dependent variable y
winRateCent = np.array([0.2619047619, 0.2023809524, 0.1071428571, 0.1428571429, 0.1388888889,
    0.08333333333, 0.04761904762, 0.05952380952, 0.04166666667, 0.03846153846,
    0.04761904762, 0.04166666667, 0.05, 0, 0, 0, 0, 0.02083333333])

# Your data remains the same...

# Assuming killsAve and rankPtsAve are your variables

# Construct matrix A: [x^2, x, constant]
A_kills = np.vstack((killsAve ** 2, killsAve, np.ones_like(killsAve))).T
A_healing = np.vstack((healing ** 2,healing, np.ones_like(healing))).T
A_endGameKills = np.vstack((endGameKills ** 2,endGameKills, np.ones_like(endGameKills))).T
# Apply least squares formula
coefficients_kills, _, _, _ = np.linalg.lstsq(A_kills, avePtsArray, rcond=None)
coefficients_healing, _, _, _ = np.linalg.lstsq(A_healing, avePtsArray, rcond=None)
coefficients_endGameKills, _, _, _ = np.linalg.lstsq(A_endGameKills, avePtsArray, rcond=None)
# Generate predicted values based on the model
predicted_avePts_kills = np.dot(A_kills, coefficients_kills)
predicted_avePts_healing = np.dot(A_healing, coefficients_healing)
predicted_avePts_endGameKills = np.dot(A_endGameKills, coefficients_endGameKills)
# Create two separate 2D plots
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

# Plotting killsAve against avePtsArray
ax1.scatter(killsAve, avePtsArray, c='r', label='Data points')
ax1.plot(killsAve, predicted_avePts_kills, color='blue', label='Regression line')
ax1.set_xlabel('killsAve')
ax1.set_ylabel('Ave Pts')
ax1.legend()

# Plotting rankPtsAve against avePtsArray
ax2.scatter(healing, avePtsArray, c='b', label='Data points')
ax2.plot(healing, predicted_avePts_healing, color='red', label='Regression line')
ax2.set_xlabel('healing')
ax2.set_ylabel('Ave Pts')
ax2.legend()


# Plotting rankPtsAve against avePtsArray
ax3.scatter(endGameKills, avePtsArray, c='b', label='Data points')
ax3.plot(endGameKills, predicted_avePts_endGameKills, color='red', label='Regression line')
ax3.set_xlabel('end Game Kills')
ax3.set_ylabel('Ave Pts')
ax3.legend()
plt.show()
