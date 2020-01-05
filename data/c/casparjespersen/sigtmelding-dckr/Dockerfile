FROM ubuntu:16.04

RUN apt-get update && apt-get install -y python3-pip libgtk2.0-dev

COPY requirements.txt ./

RUN rm /usr/bin/python \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && pip install --upgrade pip \
    && pip install -r requirements.txt --no-cache-dir \
    && apt-get purge --auto-remove