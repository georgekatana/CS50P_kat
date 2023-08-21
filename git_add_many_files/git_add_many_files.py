import os
import subprocess

# Path to the directory
base_path = r"D:\onedrive kat\OneDrive\CS50P_kat"

# Get a list of all directories in the path
directories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

# Create a text file to store the directory names
with open("directory_list.txt", "w") as file:
    for directory in directories:
        # Write the directory name followed by "/name.py" to the text file
        file.write(f"{directory}/{directory}.py\n")

print("Directory names appended to 'directory_list.txt'")

# Now let's use git add for the files listed in directory_list.txt
with open("directory_list.txt") as file:
    lines = file.readlines()
    for line in lines:
        if line!="git_add_many_files/git_add_many_files.py":
            file_path = os.path.join(base_path, line.strip())
            subprocess.run(["git", "add", file_path])

print("Git add completed for the listed files")
