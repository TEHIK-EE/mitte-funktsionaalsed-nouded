#!/usr/bin/env python3

import re
import sys
from pathlib import Path

def highlight_sections(content):
    # Highlight tables with a light gray background
    content = re.sub(
        r'(\|[^\n]+\n\|[-:]+\n)((?:\|[^\n]+\n)+)',
        r'\1<div style="background-color: #f5f5f5; padding: 10px; margin: 10px 0;">\2</div>',
        content
    )
    
    # Highlight requirements with a light blue background
    content = re.sub(
        r'(### [^\n]+\n\n)([^\n]+(?:shall|must|should|will|may)[^\n]+\n)',
        r'\1<div style="background-color: #e6f3ff; padding: 10px; margin: 10px 0; border-left: 4px solid #0066cc;">\2</div>',
        content
    )
    
    # Highlight notes and important information with a light yellow background
    content = re.sub(
        r'(> Note:.*?\n)',
        r'<div style="background-color: #fff3cd; padding: 10px; margin: 10px 0; border-left: 4px solid #ffc107;">\1</div>',
        content
    )
    
    return content

def process_file(input_file):
    print(f"Processing {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    highlighted_content = highlight_sections(content)
    
    output_file = input_file.parent / f"{input_file.stem}.highlighted{input_file.suffix}"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(highlighted_content)
    
    print(f"Created highlighted version: {output_file}")
    return output_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python highlight.py <markdown_file1> [markdown_file2 ...]")
        sys.exit(1)
    
    processed_files = []
    for file_path in sys.argv[1:]:
        input_file = Path(file_path)
        if not input_file.exists():
            print(f"Error: File {file_path} does not exist")
            continue
        processed_files.append(process_file(input_file))
    
    return processed_files

if __name__ == "__main__":
    main() 