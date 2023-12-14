import os

# The OS module allows you to interact with the operating system.

# Current Working Directory
curr_work_dir = os.getcwd()
print("The current working directory:", curr_work_dir)

# Change Directory
change_dir = '/tmp'
os.chdir(change_dir)
print("Changed directory to:", os.getcwd())

# Joining Directory Names
directory = 'my_new_dir'
parent_dir = '/home/steve/Desktop'
path = os.path.join(parent_dir, directory)
print("The new full path is:", path)

# Creating a New Directory
if not os.path.exists(path):
    os.mkdir(path)

# Create Directory Recursively
# Creates all the missing directories down to the new directory
deep_path = os.path.join(path, 'bilbo/baggins')
print("\nThe deep_path is", deep_path)
if not os.path.exists(deep_path):
    os.makedirs(deep_path)

# Listing Files and Directories
dir_list = os.listdir('/home/steve/Desktop')
print("\nFiles and directories in ", parent_dir, ":")
print(dir_list)

# Removing Files
file = 'delete_me.txt'
file_path = os.path.join(deep_path, file)
print("\nDeleting file:", file_path)
if os.path.exists(file_path):
    os.remove(file_path)

# Removing Directories
remove_dir = '/home/steve/Desktop/my_new_dir/bilbo/baggins'
print("\nDeleting Directory:", remove_dir)
if os.path.exists(remove_dir):
    os.rmdir(remove_dir)
