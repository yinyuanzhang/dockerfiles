FROM letsdeal/php:7.3-apache

RUN apt-get update \
  && apt-get install -y fontconfig fonts-roboto libjpeg62-turbo libxrender1 xfonts-75dpi xfonts-base \
  && apt-get install -t buster fonts-roboto-slab

RUN curl -LO https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb \
 && dpkg -i wkhtmltox_0.12.5-1.stretch_amd64.deb \
 && rm wkhtmltox_0.12.5-1.stretch_amd64.deb
