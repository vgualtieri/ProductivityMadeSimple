from collections import Counter
import json


def count_element_repetitions(input_list):
    element_counts = Counter(input_list)
    output_list = [[element, count] for element, count in element_counts.items()]
    return output_list


def load_activities(path):
    activities = []
    # Load the data from data.txt and append each string to data_list
    with open(f"{path}", "r") as file:
        for line in file:
            # Split each line based on commas and add the strings to the data_list
            activities.extend(line.strip().split(','))
    return activities


def load_timeslots():
    time_slots = [
        "00:00", "00:30", "01:00", "01:30", "02:00", "02:30", "03:00", "03:30",
        "04:00", "04:30", "05:00", "05:30", "06:00", "06:30", "07:00", "07:30",
        "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
        "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30",
        "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30",
        "20:00", "20:30", "21:00", "21:30", "22:00", "22:30", "23:00", "23:30",
    ]
    return time_slots


# Function to load the existing JSON data from the file
def load_json_data(file_name):
    try:
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

# Function to save the updated JSON data to the file
def save_json_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)

def update_data_entry(data, project_code, scope_code, task_code, date, time, file_name):
    # Convert input variables to strings to ensure consistency
    project_code = str(project_code)
    scope_code = str(scope_code)
    task_code = str(task_code)
    date_to_update = str(date)

    # Check if the project code exists in the data
    if project_code in data:
        if scope_code in data[project_code]:
            if task_code in data[project_code][scope_code]:
                # Update the time_slots for the specified date
                if date_to_update not in data[project_code][scope_code][task_code]["dates"]:
                    print(project_code, scope_code)

                    dates = data[project_code][scope_code][task_code]["dates"]
                    dates.append(date_to_update)
                    data[project_code][scope_code][task_code]["dates"] = dates

                    durations =  data[project_code][scope_code][task_code]["duration"]
                    durations.append(time)
                    data[project_code][scope_code][task_code]["duration"] = durations
                    # Save the updated data back to the JSON file
                    save_json_data(file_name, data)
                    print("Data updated successfully!")
                else:
                    print("Nothing changed, looks like you want to overwrite an already written date")
            else:
                data[project_code][scope_code][task_code] = {
                    "dates": [date_to_update],
                    "duration": [time]
                }
                # Save the updated data back to the JSON file
                save_json_data(file_name, data)
                print("Data updated successfully 2!")
        else:
            data[project_code][scope_code] = {
                task_code: {
                    "dates": [date_to_update],
                    "duration": [time]
                }
            }
            # Save the updated data back to the JSON file
            save_json_data(file_name, data)
            print("Data updated successfully 3!")
    else:
        data[project_code] = {
            scope_code: {
                task_code: {
                    "dates": [date_to_update],
                    "duration": [time]
                }
            }
        }
        # Save the updated data back to the JSON file
        save_json_data(file_name, data)
        print("Data updated successfully 4!")
        return data






# def update_data_entry(data, project_code, scope_code, task_code, date, time, file_name):
#     # Assuming you have the following inputs for the new data
#     project_code = f"{project_code}"
#     scope_code = f"{scope_code}"
#     task_code = f"{task_code}"
#     date_to_update = f"{date}"
#     new_time = time
#
#     # Check if the project code and activity exist in the data
#     if project_code in data and scope_code in data[project_code] and task_code in data[project_code][scope_code]:
#         # Update the time_slots for the specified date
#         data[project_code][scope_code][task_code]["dates"] = data[project_code][scope_code][task_code]["dates"].append(date_to_update)
#         data[project_code][scope_code][task_code]["duration"] = data[project_code][scope_code][task_code]["duration"].append(new_time)
#         # Save the updated data back to the JSON file
#         save_json_data(file_name, data)
#
#         print("Data updated successfully!")
#
#     elif project_code in data and scope_code in data[project_code]:
#         data[project_code][scope_code]
#
#
#
#
#
#
#
#
#
#
# def add_new_entry(project_code, scope_code, task_code, dates, time_slots):
#     if project_code not in data:
#         data[project_code] = {}
#     if scope_code not in data[project_code]:
#         data[project_code][scope_code] = {}
#     if task not in data[project_code][scope_code]:
#         data[project_code][scope_code][task_code] = {}
#     data[project_code][scope_code][task_code] = {
#         "dates": dates,
#         "time_slots": time_slots
#     }