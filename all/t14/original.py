import json
import os
import glob


def pick_json_file(parent_directory):
    # list all files in the parent directory that have a .json extension.
    json_files = glob.glob(os.path.join(parent_directory, '*.json'))
    json_files = [string for string in json_files if "report" in string]

    # display the JSON files.
    print("Please select a JSON file to load:")
    for idx, file_name in enumerate(json_files):
        print(f"{idx}: {file_name}")

    # prompt the user to select a file by number.
    selected_index = int(input("Enter the number of the JSON file you want to read: "))
    selected_file_path = json_files[selected_index]

    # read the selected JSON file.
    with open(selected_file_path) as file:
        content = json.load(file)

    return content