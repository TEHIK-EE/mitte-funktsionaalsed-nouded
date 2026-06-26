#!/bin/bash
set -e

cd /app

/usr/local/bin/marked -i input/mittefunktsionaalsed-nouded.md -o temp.html
/usr/bin/python3 inject_html.py template.html temp.html final.html
/usr/bin/wkhtmltopdf --enable-local-file-access \
    --orientation landscape \
    --margin-top 20 \
    --margin-bottom 20 \
    --margin-left 20 \
    --margin-right 20 \
    final.html output/mittefunktsionaalsed-nouded.pdf

/bin/rm temp.html final.html

echo "PDFs generated in /app/output" 