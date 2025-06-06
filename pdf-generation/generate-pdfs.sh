#!/bin/bash
set -e

cd /app

/usr/bin/python3 highlight.py input/mittefunktsionaalsed-nouded.md input/mittefunktsionaalsed-nouded.en.md

# Estonian PDF
/usr/local/bin/marked -i input/mittefunktsionaalsed-nouded.highlighted.md -o temp.html
/usr/bin/python3 inject_html.py template.html temp.html final.html
/usr/bin/wkhtmltopdf --enable-local-file-access \
    --orientation landscape \
    --margin-top 20 \
    --margin-bottom 20 \
    --margin-left 20 \
    --margin-right 20 \
    final.html output/mittefunktsionaalsed-nouded.pdf

# English PDF
/usr/local/bin/marked -i input/mittefunktsionaalsed-nouded.en.highlighted.md -o temp.html
/usr/bin/python3 inject_html.py template.html temp.html final.html
/usr/bin/wkhtmltopdf --enable-local-file-access \
    --orientation landscape \
    --margin-top 20 \
    --margin-bottom 20 \
    --margin-left 20 \
    --margin-right 20 \
    final.html output/mittefunktsionaalsed-nouded.en.pdf

/bin/rm temp.html final.html input/mittefunktsionaalsed-nouded*.highlighted.md

echo "PDFs generated in /app/output" 