import numpy as np

def accept_range(arr):
    ret_range = []
    ret_range.append(np.min(arr))
    ret_range.append(np.max(arr))
    return ret_range

def validate_range(val, range_):
    if (len(range_) != 2):
        print("not an accepted range")
        return None
    if (val >= range_[0] and val <= range_[1]):
        return val
    else: 
        print("This is not within the accepted range")
        input_ = float(input(f"Please type a number between accepted range ({range_[0]} and {range_[1]})"))
        return validate_range(input_, range_)
        
def kills_endgame_condition(result_keys, result_values):
    idx_kills = result_keys.index('1') if '1' in result_keys else None
    idx_endGame = result_keys.index('2') if '2' in result_keys else None
    if idx_kills is not None and idx_endGame is not None:
        if result_values[idx_endGame] > result_values[idx_kills]:
            return False
    return True