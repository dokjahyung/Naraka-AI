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
# Assuming kills and rankPtsAve are your variables
interaction_term = killsAve * rankPtsAve

# Construct matrix A: [x^2, x, z, constant]
Xsq = killsAve ** 2
Xcu = killsAve ** 3
Xqu = killsAve ** 4
Zsq = rankPtsAve ** 2
Zcu = rankPtsAve ** 3
Zqu = rankPtsAve ** 4


X = killsAve
Z = rankPtsAve
b = np.ones_like(killsAve)
Quart = np.vstack((Xqu, Xcu, Xsq, X, Zqu, Zcu, Zsq, Z, b)).T
CUB = np.vstack((Xcu, Xsq, X, Zcu, Zsq, Z, b)).T
SQ = np.vstack((Xsq, X, Zsq, Z, b)).T
# Apply least squares formula
betaQu = np.linalg.inv(Quart.T @ Quart) @ Quart.T @ avePtsArray
betaCUB = np.linalg.inv(CUB.T @ CUB) @ CUB.T @ avePtsArray
betaSQ = np.linalg.inv(SQ.T @ SQ) @ SQ.T @ avePtsArray
# Print the coefficients
print("Coefficients:", betaCUB)
print("Coefficients:", betaSQ)




# Generate predicted values of winRateCent based on the model
predicted_avePts_XCUB = (
    betaCUB[0] * Xcu +
    betaCUB[1] * Xsq +
    betaCUB[2] * X +
    betaCUB[6]  # Constant term
)

# Generate predicted values of winRateCent based on the model
# Assuming Xsq and Zsq represent the squared terms for killsAve and rankPtsAve respectively
predicted_avePts_ZCUB = (       # Coefficient for Z squared term
    betaSQ[0] * Zcu +  # Coefficient for the interaction term
    betaSQ[1] * Zsq +          # Coefficient for X linear term
    betaSQ[2] * Z +          # Coefficient for Z linear term
    betaSQ[4]# Constant term
)


# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111)

# Plotting the data points
ax.scatter(killsAve, rankPtsAve, avePtsArray, c='r', marker='o')

# Plotting the best-fit line
ax.plot(killsAve, rankPtsAve, predicted_avePts_XCUB, color='blue')
ax.plot(killsAve, rankPtsAve, predicted_avePts_ZCUB, color='red')
# Set labels for axes
ax.set_xlabel('killsAve')
ax.set_ylabel('Ave Pts')

plt.show()