FROM debian:buster

RUN sed -i "s/httpredir/ftp2.fr/g" /etc/apt/sources.list \
 && apt-get update -y -qq \
 && apt-get install -y -qq --no-install-recommends locales python2 python2-dev python-virtualenv build-essential git \
 && rm -rf /var/lib/apt/lists/*

RUN echo 'fr_FR.UTF-8 UTF-8' > /etc/locale.gen \
 && locale-gen

ENV LANG=fr_FR.UTF-8

RUN ln /usr/lib/python2.7/dist-packages/virtualenv.py /usr/lib/python2.7/dist-packages/venv.py
RUN ln -f /usr/bin/python2 /usr/bin/python3

