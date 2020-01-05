FROM ubuntu:bionic

RUN apt-get update && apt-get install -y --no-install-recommends \
    language-pack-en \
    apt-transport-https \
    build-essential \
    curl \
    gosu \
    gnupg2 \
    gettext \
    ipython3 \
    libssl-dev \
    libffi-dev \
    pngquant \
    python3 \
    python3-dev \
    python3-setuptools \
    python3-wheel \
    python3-pip

ADD requirements.txt /usr/local/etc/requirements.txt
RUN pip3 install -r /usr/local/etc/requirements.txt

ADD get_secrets.py /usr/local/bin/get_secrets.py

ENV LANG en_GB.UTF-8
