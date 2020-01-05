# -----------------------------------------------------------------------------
# grip - convert markdown files to html (https://github.com/joeyespo/grip)
# wkhtmltopdf - convert html files to PDF (https://wkhtmltopdf.org)
# -----------------------------------------------------------------------------
# Debian with grip and wkhtmltopdf (incl. qt patch). Used to convert Markdown files to PDF.
# Grip uses a modified template to remove the filename and box around the markdown content.



FROM debian:latest

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    python3 \
    python3-pip \
    fontconfig \
    libfreetype6 \
    libjpeg62-turbo \
    libpng16-16 \
    libx11-6 \
    libxcb1 \
    libxext6 \
    libxrender1 \
    xfonts-75dpi \
    xfonts-base \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install --upgrade setuptools \
    && pip3 install grip \
    && curl -Lo wkhtmltox.deb https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb \
    && dpkg -i wkhtmltox.deb \
    && rm wkhtmltox.deb

COPY grip-template.html /usr/local/lib/python3.5/dist-packages/grip/templates/index.html