
import json
import os

def parse_files(filename):
    files = []
    current_path = None
    current_content = []
    
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('---FILE_START: '):
                if current_path:
                    files.append({
                        "path": current_path,
                        "content": "".join(current_content)
                    })
                current_path = line.strip().split('---FILE_START: ')[1].replace('---', '')
                if current_path.startswith('./'):
                    current_path = current_path[2:]
                current_content = []
            elif line.strip() == '---FILE_END---':
                if current_path:
                    files.append({
                        "path": current_path,
                        "content": "".join(current_content)
                    })
                    current_path = None
                    current_content = []
            else:
                if current_path:
                    current_content.append(line)
    return files

files = parse_files('all_text_files.txt')
print(json.dumps(files, indent=2))
