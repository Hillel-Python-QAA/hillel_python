""  # pathlib

import os
from pathlib import Path

path = Path(Path.home() / "Downloads")
path1 = Path("/path/to/directory")
path_file = Path(path / "script.py")

print(path)

directories = [d for d in path.iterdir() if d.is_dir()]

print("List of directories:")
for d in directories:
    print(d)

files = [f for f in path.iterdir() if f.is_file()]

print("List of files:")
for f in files:
    print(f)

extension = ".pdf"
files_with_py_extension = [f for f in path.iterdir() if f.suffix == extension]

print(f"List of files with extension '{extension}':")
for f in files_with_py_extension:
    print(f)

print(path.exists())
print(path1.exists())

# Get path object name

print(path.name)
print(path_file)
print(path_file.name)

# Get parent object's path
print(path_file.parent)
print(path.parent)

# Get Current Working Directory
print(Path.cwd())

# Get home directory
print(Path.home())

# Change to another directory
path_cwd = Path.cwd()
print("CWD before change", Path.cwd())
os.chdir(Path.home())
print("CWD after change", Path.cwd())


## Create directory
new_directory = Path(Path.home() / "Downloads/A_NEW_DIR")
new_directory.mkdir(exist_ok=True)

new_dir_without_existing_parents = Path(new_directory / "B_NEW_DIR/C_NEW_DIR/D_NEW_DIR")
new_dir_without_existing_parents.mkdir(parents=True, exist_ok=True)

# Read file
with open(path_file, "r") as file:
    content = file.read()
    print(content)

os.chdir(path_cwd / "lecture_12")
print(Path.cwd())

# Write file
with open("example.txt", "w") as f:
    f.write("Hello, world!")

with open("example.txt", "a") as f:
    f.write("Appending new content\n")

# encoding files
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hi")
