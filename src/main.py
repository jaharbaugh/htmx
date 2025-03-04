from textnode import *
from copy_static import *
from generate_pages_recursive import *

import os
import shutil
import sys

basepath = '/'

if len(sys.argv) > 1:
    basepath = sys.argv[1]

def main():
    if os.path.exists('docs'):
        shutil.rmtree('docs')

    copy_static('static', 'docs')
    generate_pages_recursive('content', 'template.html', 'docs', basepath )

main()    