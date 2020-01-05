FROM openjdk:8-slim

# Download and install wkhtmltopdf
RUN apt-get update \
    && apt-get install -y \
        curl \
        xfonts-base \
        xfonts-75dpi \
        fontconfig \
        libxext6 \
        libjpeg62-turbo\
        libx11-6 \
        libxrender1 \
    && apt-get clean

RUN curl "https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb" -L -o "wkhtmltopdf.deb" \
    && dpkg -i ./wkhtmltopdf.deb \
    && apt-get install -f \
    && rm -rf wkhtmlto*
