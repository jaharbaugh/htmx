import os

from generate_page import *

def generate_pages_recursive(dir_path, template_path, dest_dir_path, basepath='/'):
    entries = os.listdir(dir_path)
    for entry in entries:
        entry_path = os.path.join(dir_path, entry)


        if os.path.isfile(entry_path) and entry_path.endswith('.md'):
            relative_path = os.path.relpath(entry_path, dir_path)
            dest_file = os.path.splitext(relative_path)[0] + '.html'
            dest_path = os.path.join(dest_dir_path, dest_file)
            generate_page(entry_path, template_path, dest_path, basepath)
        elif os.path.isdir(entry_path):
            dir_name = os.path.basename(entry_path)
            new_dest_dir = os.path.join(dest_dir_path, dir_name)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(entry_path, template_path, new_dest_dir, basepath)