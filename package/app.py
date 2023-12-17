import tkinter as tk
import function as fn
import prediction as pred
from prediction import avePtsArray, accepted_assists, accepted_damage, accepted_endGame, accepted_healing, accepted_kills, accepted_rank, accepted_offSpawn, accepted_yangPart, accepted_yangWin
import handle
import filepath as file

def get_checkbox_values():
    return [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get()]

def create_or_remove_text_boxes(selected_values):
    for idx, value in enumerate(selected_values):
        if value == 1 and text_boxes[idx] is None:
            text_boxes[idx] = tk.Entry(root)
            text_boxes[idx].grid(row=idx, column=1, padx=5, pady=5, sticky=tk.W)  # Use 'sticky' to align the text boxes
        elif value == 0 and text_boxes[idx] is not None:
            text_boxes[idx].destroy()
            text_boxes[idx] = None

def get_accepted_range(choice):
    ranges = {
        '1': accepted_kills,
        '2': accepted_endGame,
        '3': accepted_rank,
        '4': accepted_damage,
        '5': accepted_healing,
        '6': accepted_assists,
        '7': accepted_yangPart,
        '8': accepted_yangWin,
        '9': accepted_offSpawn
    }
    return ranges.get(choice)


def validate_range(value, range_):
    try:
        val = float(value)  # Convert value to float
        if val >= range_[0] and val <= range_[1]:
            return True
        else:
            return False
    except ValueError:
        return False


def show_error(message):
    error_label.config(text=message)

def show_selected():
    create_or_remove_text_boxes(get_checkbox_values())

def get_checkbox_values():
    return [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get()]

def create_or_remove_text_boxes(selected_values):
    for idx, value in enumerate(selected_values):
        if value == 1 and text_boxes[idx] is None:
            text_boxes[idx] = tk.Entry(root)
            text_boxes[idx].grid(row=idx, column=2, padx=5, pady=5, sticky=tk.W)  # Use 'sticky' to align the text boxes
        elif value == 0 and text_boxes[idx] is not None:
            text_boxes[idx].destroy()
            text_boxes[idx] = None


def predict_input(degree):
    selected_values = get_checkbox_values()
    selected_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    results = get_text_box_values(selected_labels)
    result_keys, result_values = process_results(results)
    
        # Ensure 'End Game Kills' are not greater than 'Kills'
    if handle.kills_endgame_condition(result_keys, result_values) == False:
        show_error("End Game Kills cannot be greater than Kills")
        return

    predicted_y = pred.use_model_predict(result_keys, result_values, avePtsArray, degree)
    display_predicted_value(predicted_y)
    show_error("")

def get_selected_items(values, labels):
    return [label for value, label in zip(values, labels) if value == 1]


def create_or_remove_text_boxes(selected_values):
    global text_boxes  # Declare 'text_boxes' as a global variable to modify it inside the function
    for idx, value in enumerate(selected_values):
        if value == 1 and text_boxes[idx] is None:
            text_boxes[idx] = tk.Entry(root)
            text_boxes[idx].grid(row=idx, column=2, padx=5, pady=5, sticky=tk.W)  # Use 'sticky' to align the text boxes
        elif value == 0 and text_boxes[idx] is not None:
            text_boxes[idx].destroy()
            text_boxes[idx] = None


def get_text_box_values(labels):
    results = []
    for item_number in labels:
        idx = int(item_number) - 1
        if text_boxes[idx] is not None:
            results.append((item_number, text_boxes[idx].get()))
    return results

def process_results(results):
    result_keys = []
    result_values = []
    for item in results:
        idx = int(item[0]) - 1
        value = item[1]
        if text_boxes[idx] is not None:
            if value == '':
                error_message = f"Value cannot be empty"
                show_error(error_message)
                return None, None  # Return None for both keys and values
            else:
                if validate_range(value, get_accepted_range(item[0])):
                    result_keys.append(item[0])
                    result_values.append(float(value))
                else:
                    error_message = f"Invalid value: '{value}' or no valid range"
                    show_error(error_message)
                    return None, None  # Return None for both keys and values
    return result_keys, result_values


def display_predicted_value(value):
    output_label.config(text=f"Predicted Y: {value}")

root = tk.Tk()
root.title("Naraka AI Trios")
window_width = 850
window_height = 600

# Set the window size using geometry method (width x height)
root.geometry(f"{window_width}x{window_height}")

# Add image file 
bg = tk.PhotoImage(file = file.resource_path("moonsun.png"))
bg_label = tk.Label(root, image=bg)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()
var7 = tk.IntVar()
var8 = tk.IntVar()
var9 = tk.IntVar()

checkboxes = [
    ("Kills", var1),
    ("End Game Kills", var2),
    ("Rank Points", var3),
    ("Damage", var4),
    ("Healing", var5),
    ("Assists", var6),
    ("Yang Participation", var7),
    ("Yang Win Rate", var8),
    ("Off Spawn Wins", var9)
]

text_boxes = [None] * len(checkboxes)

for idx, (text, var) in enumerate(checkboxes):
    checkbox = tk.Checkbutton(root, text=text, variable=var, command=show_selected)
    checkbox.grid(row=idx, column=1, sticky=tk.W)

kills_label = tk.Label(root, text=f"Kills accepted range ({accepted_kills[0]} and {accepted_kills[1]})", fg="green")  # Customize color if needed
kills_label.grid(row=len(checkboxes) + 5, columnspan=2)
endGame_label = tk.Label(root, text=f"End Game Kills accepted range ({accepted_endGame[0]} and {accepted_endGame[1]})", fg="green")  # Customize color if needed
endGame_label.grid(row=len(checkboxes) + 7, columnspan=2)
rank_label = tk.Label(root, text=f"Rank Points accepted range ({accepted_rank[0]} and {accepted_rank[1]})", fg="green")  # Customize color if needed
rank_label.grid(row=len(checkboxes) + 9, columnspan=2)
damage_label = tk.Label(root, text=f"Damage accepted range ({accepted_damage[0]} and {accepted_damage[1]})", fg="green")  # Customize color if needed
damage_label.grid(row=len(checkboxes) + 12, columnspan=2)
healing_label = tk.Label(root, text=f"Healing accepted range ({accepted_healing[0]} and {accepted_healing[1]})", fg="green")  # Customize color if needed
healing_label.grid(row=len(checkboxes) + 14, columnspan=2)
assists_label = tk.Label(root, text=f"Assists accepted range ({accepted_assists[0]} and {accepted_assists[1]})", fg="green")  # Customize color if needed
assists_label.grid(row=len(checkboxes) + 15, columnspan=2)
yangPart_label = tk.Label(root, text=f"Yang Participation accepted range ({accepted_yangPart[0]} and {accepted_yangPart[1]})", fg="green")  # Customize color if needed
yangPart_label.grid(row=len(checkboxes) + 16, columnspan=2)
yangWin_label = tk.Label(root, text=f"Yang Win Rate accepted range ({accepted_yangWin[0]} and {accepted_yangWin[1]})", fg="green")  # Customize color if needed
yangWin_label.grid(row=len(checkboxes) + 17, columnspan=2)
offSpawn_label = tk.Label(root, text=f"Off Spawn Kill accepted range ({accepted_offSpawn[0]} and {accepted_offSpawn[1]})", fg="green")  # Customize color if needed
offSpawn_label.grid(row=len(checkboxes) + 18, columnspan=2)

error_label = tk.Label(root, text="", fg="red")  # Customize color if needed
error_label.grid(row=len(checkboxes) + 3, columnspan=2)  # Adjust position based on your layout

output_label = tk.Label(root, text="Predicted Y: ")
output_label.grid(row=len(checkboxes) + 1, columnspan=2)

linear_button = tk.Button(root, text="Predict Total Score w/ Linear Least Square Regression", command=lambda: predict_input(1))
linear_button.grid(row=len(checkboxes), column=0, columnspan=2, pady=10)


cubic_button = tk.Button(root, text="Predict Total Score w/ Cubic Least Square Regression", command=lambda: predict_input(3))
cubic_button.grid(row=len(checkboxes)+2, column=0, columnspan=2, pady=10)

vertical_shift = 50
root.mainloop()
