import os
from extract_title import *
from markdowntohtmlnode import *

def generate_page(from_path, template_path, destination, BASEPATH='/'):
    print(f'Generating page from {from_path} to {destination} using {template_path}')
    
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    for line in markdown_content.split('\n'):
        if "didn't ruin it" in line:
            print(f"Found line: {line}")
            # Process just this line to see what happens
            test_node = paragraph_to_html_node(line)
            print(f"HTML output: {test_node.to_html()}")
    
    
    with open(template_path, 'r') as file:
        template = file.read()

    title = extract_title(markdown_content)

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    final_html = template.replace('{{ Title }}', title)
    final_html = final_html.replace('{{ Content }}', html_content)
    final_html = final_html.replace('href="/', f'href="{BASEPATH}')
    final_html = final_html.replace('src="/', f'src="{BASEPATH}')
    os.makedirs(os.path.dirname(destination), exist_ok=True)


    with open(destination, 'w') as file:
        file.write(final_html)

    
