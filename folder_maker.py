import os

# Get inputs from the user
start_point = int(input("Enter Starting Point: "))
end_point = int(input("Enter upto which you want: "))
suffix = input("Enter suffix: ")

# Create folders in the given range
for i in range(start_point, end_point + 1):
    folder_name = f"{i}{suffix}"
    os.makedirs(folder_name, exist_ok=True)  # Creates folder, and won't raise an error if it already exists
    print(f"Folder created: {folder_name}")
