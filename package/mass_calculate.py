import function as fn
from prediction import killsAve, endGameKills, avePtsArray, rankPtsAve, healing, damage, assists
import itertools

#perma nested loops for the win
def factorial_rsq(factor, y):
    calc_dict = {}
    for i in range(1, factor):
        for j in range(1, factor):
            for combo_length in range(1, factor + 1):  # Generate combinations of different lengths
                combos = itertools.combinations(range(1, factor + 1), combo_length)
                for combo in combos:
                    var = [str(val) for val in combo]
                    if len(set(var)) == len(var):  # Check for unique elements in the combination
                        if calc_dict.get(tuple(var)) is None and calc_dict.get(tuple(var[::-1])) is None:
                            if len(var) == 1:
                                calc_dict[tuple(var)] = fn.r_squared_cubic(var[0], y)
                            else:
                                calc_dict[tuple(var)] = fn.r_squared_cubic(var, y)
                            print(f"{var} : {calc_dict[tuple(var)]}")