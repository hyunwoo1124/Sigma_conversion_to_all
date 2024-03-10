import os
import shutil
from sigmaiq import SigmAIQBackend
from sigma.rule import SigmaRule
import json

directory = input("Enter the directory where you wish to copy contents from: ")
key = input("Whats the key string you are looking for?: ")
destination = input("Enter the new directory you wish to copy to: ")

os.makedirs(destination, exist_ok=True)
key_found = False

for root, _, files in os.walk(directory):
    for filename in files:
        if key in filename:
            key_found = True
            file_path = os.path.join(root, filename)
            shutil.copy(file_path, destination)
            print(f"File '{filename}' is copied to '{destination}'")

if not key_found:
    print(f"String '{key}' was never found in directory '{directory}'")

directory = destination
files = os.listdir(directory)
for file_name in files:
    filepath = os.path.join(directory, file_name)

    if os.path.isfile(filepath):
        with open(filepath, 'r') as my_file:
            sigma_rule_all = my_file.read()
        sigma_rule_all = SigmaRule.from_yaml(sigma_rule_all)
        output = SigmAIQBackend.create_all_and_translate(sigma_rule_all)

        # Convert the output dictionary to a JSON string
        output_json = json.dumps(output, indent=4)  # Assuming you want an indented JSON string

        output_filename = f"translated_{file_name}"
        output_filepath = os.path.join(directory, output_filename)

        with open(output_filepath, 'w') as output_file:
            output_file.write(output_json)  # Write the JSON string to the file
        print(f"Translated rule saved to {output_filepath}")
    else:
        print("failed")
