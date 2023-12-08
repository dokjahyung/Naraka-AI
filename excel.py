import pandas as pd
import numpy as np
import tensorflow as tf

# Provided arrays
game1TotalPoints = np.array([206.20, 162.10, 157.30, 142.10, 127.70, 127.20, 112.90, 104.70, 90.50, 79.60, 82.20, 79.20, 74.00, 65.80])
game2TotalPoints = np.array([179.8, 163.6, 180.2, 149.6, 152, 130.2, 142, 101.2, 93.4, 109.6, 104.6, 90.4, 42.2, 43.6])
game3TotalPoints = np.array([139.9-39.7, 129-30.8, 122.9-45.9, 118.5-49.6, 105.7-30.2, 105.3-39.2, 96.6-29.1, 95.7-43.3, 83.1-34.8, 79.8-39.4, 71.3-27.9, 58.1-27.2, 53.1-23.6, 45.8-23.4])

game1KillsAve = np.array([9.2, 8.2, 8, 7.4, 7.2, 6.2, 6.2, 5.8, 4.6, 4.4, 4.4, 4.4, 4.2, 3.8])
game2KillsAve = np.array([8.3, 7.5, 8.8, 6.8, 8.2, 7.2, 6.8, 6.5, 4.5, 5.8, 6.3, 5, 3, 2.8])
game3KillsAve = np.array([8.8, 9.2, 7.5, 7.8, 7.2, 7.7, 6.7, 5.8, 5, 4.8, 6.2, 3.7, 3.7, 2.5])


game1RankPtsAve = np.array([3, 1.8, 1.5, 1.5, 1.9, 1, 1, 0.8, 1.1, 0.8, 0.8, 0.7, 0.7, 0.8])
game2RankPtsAve = np.array([2.3, 2.2, 2, 1.7, 1.2, 2.2, 1.2, 1, 1.2, 0.8, 0.7, 0.2, 0.2, 0.6])
game3RankPtsAve = np.array([2.9, 2.5, 1.8, .9, 1.9, .8, 1.8, 1.1, 1.3, .7, .2, .6, .5, .7])

game1EndGameKills = np.array([4.3, 2.3, 2.1, 2.6, 1.2, 1, 1.3, 1.3, 1.1, 0.8, 1.5, 0.6, 0.3, 0.4])
game2EndGameKills = np.array([3.2, 2.7, 2.2, 1.8, 1.3, 1.3, 1.2, 0.8, 0.8, 0.5, 0.2, 0, 0, 0])
game3EndGameKills = np.array([5, 2.3, 2.5, 2.3, 1.7, .8, 1.3, .8, .5, .2, 0, .8, .5, 0])

game1Healing = np.array([25462.80, 23775.10, 26110.30, 25027.90, 20871.10, 24847.20, 19557.70, 17014.70, 22304.00, 16935.30, 16394.90, 18502.00, 16598.70, 16904.60])
game2Healing = np.array([30805, 25392.2, 25180.4, 21256.1, 20698.2, 18997.8, 18007.3, 17773.1, 17756.6, 16651.6, 16097.5, 14364.3, 13664.7, 9060.3])
game3Healing = np.array([31772.1, 26475, 18710.6, 21635.6, 31073.4, 24787.9, 27313, 19291.7, 19258.3, 21362.1, 15192.2, 16876.8, 13288.2, 12623.5])

game1Damage = np.array([46735.1, 29678, 33205.9, 34882.6, 28798.1, 29474.8, 33250.6, 25500.6, 27269.9, 27327.4, 27264.4, 27288, 20586.5, 22071.6])
game2Damage = np.array([34386.8, 34700.7, 40371.8, 33337.8, 38400.1, 34785.9, 29513.1, 32524.7, 23647.5, 32309.3, 34243.3, 24461, 14219.5, 15729])
game3Damage = np.array([41875.1, 46674.8, 35567.7, 33127, 45287.7, 35189.7, 37849.7, 27758.7, 23671.6, 28612.6, 26021.2, 20868.3, 20678.2, 22020.2])

game1Assists = np.array([13.5, 11.6, 11.5, 9.2, 7.3, 9.4, 9.1, 7.8, 5.6, 6.1, 5, 6, 5.3, 4.5])
game2Assists = np.array([13.2, 4, 11.8, 3.3, 5.3, 10.8, 8.3, 10.7, 6.5, 9.3, 11.8, 7, 10.8, 9])
game3Assists = np.array([13, 12.5, 10.5, 10.7, 11.8, 10.3, 8.2, 6.8, 6.7, 6.3, 7.8, 4.7, 5, 3.8])
# Include other arrays similarly for game 2 and game 3...

# Create a dictionary with the arrays
data = {
    'Game 1 Total Points': game1TotalPoints/12,
    'Game 2 Total Points': game2TotalPoints/12,
    'Game 3 Total Points': game3TotalPoints/6,
    'Game 1 Kills Average': game1KillsAve,
    'Game 2 Kills Average': game2KillsAve,
    'Game 3 Kills Average': game3KillsAve,
    'Game 1 Rank Points Average': game1RankPtsAve,
    'Game 2 Rank Points Average': game2RankPtsAve,
    'Game 3 Rank Points Average': game3RankPtsAve,
    'Game 1 End Game Kills': game1EndGameKills,
    'Game 2 End Game Kills': game2EndGameKills,
    'Game 3 End Game Kills': game3EndGameKills,
    'Game 1 Healing': game1Healing,
    'Game 2 Healing': game2Healing,
    'Game 3 Healing': game3Healing,
    'Game 1 Damage': game1Damage,
    'Game 2 Damage': game2Damage,
    'Game 3 Damage': game3Damage,
    'Game 1 Assists': game1Assists,
    'Game 2 Assists': game2Assists,
    'Game 3 Assists': game3Assists,
    # Include other arrays similarly for game 2 and game 3...
}

# Create a DataFrame using pandas
df = pd.DataFrame(data)

dataset = tf.data.Dataset.from_tensor_slices(dict(df))

# Iterate through the dataset (for example, printing the values)
for element in dataset:
    print(element)
