
FROM python:3.8-buster
MAINTAINER ONIT <weare@onit.ws>

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1

# Update and install packages recomended by Django documentation:
# https://docs.djangoproject.com/ja/1.9/ref/contrib/gis/install/geolibs/
# and extra needed packages

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update -y --no-install-recommends && \
    apt-get install --auto-remove -y \
      apt-utils \
      binutils \
      libproj-dev \
      gdal-bin \
      postgis \
      curl \
      locales \
      gettext \ 
      apt-transport-https \
      curl \
      python-dev \
      build-essential \
      libblas-dev \
      liblapack-dev \ 
      gfortran \
      software-properties-common \
      google-chrome-stable && \
    curl -sL https://deb.nodesource.com/setup_10.x | bash - && \
    apt install nodejs && \
    rm -rf /var/lib/apt/lists/*


RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && /usr/sbin/locale-gen
