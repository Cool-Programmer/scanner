import os


# Create folder for saving files.
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Write on a file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()
