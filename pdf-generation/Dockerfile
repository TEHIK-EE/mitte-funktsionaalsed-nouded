FROM node:24-slim
LABEL org.opencontainers.image.authors="oliver.vaga@tehik.ee"
LABEL org.opencontainers.image.title="PDF Generator for TEHIK MFN Markdown"

# Install required packages
RUN apt-get update && apt-get install -y \
    coreutils \
    python3 \
    python3-pip \
    wkhtmltopdf \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir -p input output && \
    npm install -g marked-cli@0.3.1 && \
    ln -sf /usr/local/lib/node_modules/marked-cli/node_modules/marked/bin/marked /usr/local/bin/marked

ENV PATH="/usr/local/bin:$PATH"

COPY template.html highlight.py inject_html.py generate-pdfs.sh ./
RUN chmod +x highlight.py && \
    chmod +x inject_html.py && \
    chmod +x generate-pdfs.sh

CMD ["/app/generate-pdfs.sh"] 