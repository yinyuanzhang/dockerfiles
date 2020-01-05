FROM python:3.8
MAINTAINER Michal Čihař <michal@cihar.com>
RUN apt update && \
    apt install -y \
        graphviz \
        chromium-driver \
        git-svn \
        libcairo-dev \
        gir1.2-pango-1.0 \
        libgirepository1.0-dev \
        libenchant1c2a \
        g++ \
        libtesseract-dev \
        libleptonica-dev \
        libacl1-dev \
        tesseract-ocr-eng \
        gettext \
        locales \
        postgresql-client \
        default-mysql-client && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
COPY requirements.txt /tmp/
RUN pip install Cython
RUN pip install --no-cache-dir -r /tmp/requirements.txt https://github.com/codecov/codecov-python/archive/master.zip
