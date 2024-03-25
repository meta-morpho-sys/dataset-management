import os


import os

def get_directory_path(prompt_message, default_directory="Downloads"):
    relative_directory = input(prompt_message).strip()
    if not relative_directory:
        relative_directory = default_directory
    return os.path.join(os.path.expanduser('~'), relative_directory)

def validate_directory(directory):
    if not os.path.isdir(directory):
        print(f"The path {directory} is not a valid directory.")
    else:
        print(f"Directory is set to: {directory}")

def validate_and_get_file_path(directory, default_filename="test_sheet.csv"):
    filename = input("Please enter the source file name. \nExample: < management_fees_merge.csv >: ").strip()
    if not filename:
        filename = default_filename
    file_path = f"{directory}/{filename}"
    if not os.path.isfile(file_path):
        print(f"\nError: The path {file_path} is not a valid directory.\nTIP: Check the filename and its location and rerun the program")
        exit()
    else:
        print(f"Source file is: {file_path}")
    return file_path

def ensure_directory_exists(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=True)
        print(f"Directory created at: {directory}")
    else:
        print(f"Directory is set to: {directory}")

def prepare_location():
    source_directory = get_directory_path("Please enter the source directory path relative to your home directory: ")
    validate_directory(source_directory)
    path_to_csv = validate_and_get_file_path(source_directory)
    output_directory = get_directory_path("Please enter the output directory path relative to your home directory: ")
    os.makedirs(f"{output_directory}/insights/", exist_ok=True)
    print("The source directory is:", source_directory)
    print("The output directory is:", output_directory)
    return path_to_csv, output_directory
