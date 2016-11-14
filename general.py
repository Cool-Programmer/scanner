import os


# Create folder for saving files.
def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating a folder...')
        os.makedirs(directory)

# Write on a file
def write_file(path, data):
    print('Writing...')
    f = open(path, 'w')
    f.write(data)
    f.close()
