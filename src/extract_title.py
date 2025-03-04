def extract_title(markdown):
    lines = markdown.split('\n')
    for line in lines:
        line = line.strip()        
        if line.startswith('# '):
            header = line.strip('#')
            header = header.strip()
            return header
    raise Exception("No header found")

    
    