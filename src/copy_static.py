import os
import shutil

def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)

    files = os.listdir(source)

    for file in files:
        source_path = os.path.join(source, file)
        if os.path.isfile(source_path):
            
            copy = shutil.copy(source_path, destination)
            print(copy)
        else:
            destination_path = os.path.join(destination, file)
            os.mkdir(destination_path)
            copy_static(source_path, destination_path)