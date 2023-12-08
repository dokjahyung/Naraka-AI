import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import function as fn
import sys
import matrix
import handle

#possible x values
#average kills in 6 set game
game1KillsAve = np.array([9.2, 8.2, 8, 7.4, 7.2, 6.2, 6.2, 5.8, 4.6, 4.4, 4.4, 4.4, 4.2, 3.8])
game2KillsAve = np.array([8.3, 7.5, 8.8, 6.8, 8.2, 7.2, 6.8, 6.5, 4.5, 5.8, 6.3, 5, 3, 2.8])
game3KillsAve = np.array([8.8, 9.2, 7.5, 7.8, 7.2, 7.7, 6.7, 5.8, 5, 4.8, 6.2, 3.7, 3.7, 2.5])
killsAve = np.concatenate((game1KillsAve, game3KillsAve))
accepted_kills = handle.accept_range(killsAve)
#placement points

game1RankPtsAve = np.array([3, 1.8, 1.5, 1.5, 1.9, 1, 1, 0.8, 1.1, 0.8, 0.8, 0.7, 0.7, 0.8])
game2RankPtsAve = np.array([2.3, 2.2, 2, 1.7, 1.2, 2.2, 1.2, 1, 1.2, 0.8, 0.7, 0.2, 0.2, 0.6])
game3RankPtsAve = np.array([2.9, 2.5, 1.8, .9, 1.9, .8, 1.8, 1.1, 1.3, .7, .2, .6, .5, .7])
rankPtsAve = np.concatenate((game1RankPtsAve, game3RankPtsAve))
accepted_rank = handle.accept_range(rankPtsAve)
#this was perhaps the strongest r value in the sets, kills at last 2-5 min of game
game1EndGameKills = np.array([4.3, 2.3, 2.1, 2.6, 1.2, 1, 1.3, 1.3, 1.1, 0.8, 1.5, 0.6, 0.3, 0.4])
game2EndGameKills = np.array([3.2, 2.7, 2.2, 1.8, 1.3, 1.3, 1.2, 0.8, 0.8, 0.5, 0.2, 0, 0, 0])
game3EndGameKills = np.array([5, 2.3, 2.5, 2.3, 1.7, .8, 1.3, .8, .5, .2, 0, .8, .5, 0])
endGameKills = np.concatenate((game1EndGameKills, game3EndGameKills))
accepted_endGame = handle.accept_range(endGameKills)
#healing had a stronger impact on total points than damage did. this I believe is because of how it means teams with greater survivability
#had great placement points and kill multipliers. Common misconception I found here as a veteran player is that although the game has tried to curb passive gameplay
#The strongest strategy is to be aggressive only in no risk situations and remain passive
game1Healing = np.array([25462.80, 23775.10, 26110.30, 25027.90, 20871.10, 24847.20, 19557.70, 17014.70, 22304.00, 16935.30, 16394.90, 18502.00, 16598.70, 16904.60])
game2Healing = np.array([30805, 25392.2, 25180.4, 21256.1, 20698.2, 18997.8, 18007.3, 17773.1, 17756.6, 16651.6, 16097.5, 14364.3, 13664.7, 9060.3])
game3Healing = np.array([31772.1, 26475, 18710.6, 21635.6, 31073.4, 24787.9, 27313, 19291.7, 19258.3, 21362.1, 15192.2, 16876.8, 13288.2, 12623.5])
healing = np.concatenate((game1Healing, game3Healing))
accepted_healing = handle.accept_range(healing)
#damage had a strong correlation with total points in excel but this is not useful for a player to determine anything except oppressive skill wins above all
game1Damage = np.array([46735.1, 29678, 33205.9, 34882.6, 28798.1, 29474.8, 33250.6, 25500.6, 27269.9, 27327.4, 27264.4, 27288, 20586.5, 22071.6])
game2Damage = np.array([34386.8, 34700.7, 40371.8, 33337.8, 38400.1, 34785.9, 29513.1, 32524.7, 23647.5, 32309.3, 34243.3, 24461, 14219.5, 15729])
game3Damage = np.array([41875.1, 46674.8, 35567.7, 33127, 45287.7, 35189.7, 37849.7, 27758.7, 23671.6, 28612.6, 26021.2, 20868.3, 20678.2, 22020.2])
damage = np.concatenate((game1Damage, game3Damage))
accepted_damage = handle.accept_range(damage)
#teams can only have a max of 2x there kills. in excel saw a deep correlation between assists and points. more coordinated teams tend to do well
game1Assists = np.array([13.5, 11.6, 11.5, 9.2, 7.3, 9.4, 9.1, 7.8, 5.6, 6.1, 5, 6, 5.3, 4.5])
game2Assists = np.array([13.2, 4, 11.8, 3.3, 5.3, 10.8, 8.3, 10.7, 6.5, 9.3, 11.8, 7, 10.8, 9])
game3Assists = np.array([13, 12.5, 10.5, 10.7, 11.8, 10.3, 8.2, 6.8, 6.7, 6.3, 7.8, 4.7, 5, 3.8])
assists = np.concatenate((game1Assists, game3Assists))
accepted_assists = handle.accept_range(assists)

#possible y values
#win rate %
winRateCent = np.array([0.2619047619, 0.2023809524, 0.1071428571, 0.1428571429, 0.1388888889,
    0.08333333333, 0.04761904762, 0.05952380952, 0.04166666667, 0.03846153846,
    0.04761904762, 0.04166666667, 0.05, 0, 0, 0, 0, 0.02083333333])
#total points during the 6 game set
game1TotalPoints = np.array([206.20, 162.10, 157.30, 142.10, 127.70, 127.20, 112.90, 104.70, 90.50, 79.60, 82.20, 79.20, 74.00, 65.80])
game2TotalPoints = np.array([179.8, 163.6, 180.2, 149.6, 152, 130.2, 142, 101.2, 93.4, 109.6, 104.6, 90.4, 42.2, 43.6])
game3TotalPoints = np.array([139.9-39.7, 129-30.8, 122.9-45.9, 118.5-49.6, 105.7-30.2, 105.3-39.2, 96.6-29.1, 95.7-43.3, 83.1-34.8, 79.8-39.4, 71.3-27.9, 58.1-27.2, 53.1-23.6, 45.8-23.4])
#make this for 12 instead of 6 games
game3TotalPoints = game3TotalPoints*2
TotalPoints = np.concatenate((game1TotalPoints,game3TotalPoints))
#easier way to crunch data if it's an ave
avePtsArray = TotalPoints/12
game1AvePtsArray = game1TotalPoints/12
game2AvePtsArray = game2TotalPoints/12



variable_list = []
variables = []

def predict_y_assists(assists_input):
    coefficients_assists = fn.coefficient_eq(fn.construct_cubic_matrix(assists), avePtsArray)
    # Assuming coefficients_assists contains coefficients for a cubic equation
    predicted_y = (
        coefficients_assists[0] * assists_input ** 3 +
        coefficients_assists[1] * assists_input ** 2 +
        coefficients_assists[2] * assists_input +
        coefficients_assists[3]  # Constant term
    )  # Use previously computed coefficients
    return predicted_y

def predict_y(coefficients_x, variables):
    expect_y = matrix.extend_predict(coefficients_x, variables)
    return expect_y

def prompt():
    print("")
    print("Prediction Platform")
    print("")
    print("1. Predict Average Points based on Kills")
    print("2. Predict Average Points based on End Game Kills")
    print("3. Predict Average Points based on Rank Points")
    print("4. Predict Average Points based on Damage")
    print("5. Predict Average Points based on Healing")
    print("6. Predict Average Points based on Assists")
    print("7. Predict with values")
    print("8. Stop prediction software")
    print("")

def use_model_predict(variable_list, variables, y):
    coefficients_x = fn.coefficient_eq(matrix.cubic_form(variable_list), y)
    
    predicted_y = predict_y(coefficients_x, variables)
    return predicted_y
# Function to predict y for a single input value based on user choice
def predict_y_for_input():
    global variable_list
    global variables
    global accepted_kills, accepted_healing, accepted_assists, accepted_damage, accepted_endGame, accepted_rank
    
    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
    if choice == '1':
        input_ = float(input("Enter Kills: "))
        variable_list.append(choice)
        variables.append(handle.validate_range(input_, accepted_kills))
    elif choice == '2':
        input_ = float(input("Enter End Game Kills: "))
        variable_list.append(choice)
        variables.append(handle.validate_range(input_, accepted_endGame))
    elif choice == '3':
        input_ = float(input("Enter Rank Pts: "))
        variable_list.append(choice)
        variables.append(handle.validate_range(input_, accepted_rank))
    elif choice == '4':
        input_ = float(input("Enter Damage: "))
        variable_list.append(choice)
        variables.append(handle.validate_range(input_, accepted_damage))
    elif choice == '5':
        input_ = float(input("Enter Healing: "))
        variable_list.append(choice)
        variables.append(handle.validate_range(input_, accepted_healing))
    elif choice == '6':
        input_ = float(input("Enter Assists: "))
        variable_list.append(choice)
        variables.append(handle.validate_range(input_, accepted_assists))
    elif choice == '7':
        predicted_y_ = use_model_predict(variable_list, variables, avePtsArray)
        print(f"Hello sir your total points would be: {predicted_y_}")
        variable_list = []
        variables = []
    elif choice == '8':  
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
    prompt()
    predict_y_for_input()

def prediction_software():
    prompt()
    predict_y_for_input()