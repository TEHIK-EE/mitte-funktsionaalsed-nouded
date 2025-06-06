#!/usr/bin/env python3
import sys

if len(sys.argv) != 4:
    print("Usage: python inject_html.py <template.html> <content.html> <output.html>")
    sys.exit(1)

template_path = sys.argv[1]
content_path = sys.argv[2]
output_path = sys.argv[3]

with open(template_path, 'r', encoding='utf-8') as f:
    template = f.read()
with open(content_path, 'r', encoding='utf-8') as f:
    content = f.read()

result = template.replace("{{content}}", content)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(result) 