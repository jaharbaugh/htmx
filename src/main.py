from textnode import *
from copy_static import *
from generate_pages_recursive import *

import os
import shutil


def main():
    if os.path.exists('public'):
        shutil.rmtree('public')

    copy_static('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public' )

main()    