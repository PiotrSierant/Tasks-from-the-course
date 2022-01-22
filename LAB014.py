import LAB012
import LAB013
import os

files_to_process = [
    r"C:\Users\dzd07\Desktop\Python\LAB012.py",
    r"C:\Users\dzd07\Desktop\Python\LAB013.py"
]

for file_path in files_to_process:

    with open(file_path, 'r') as file:
        print("File {} ...".format(os.path.basename(file_path)))
        source = file.read()
        exec(source)

for file_path in files_to_process:
    print(os.path.basename(file_path))