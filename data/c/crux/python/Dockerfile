FROM crux/python:latest
MAINTAINER James Mills <prologic@shortcircuitnet.au>

ONBUILD COPY requirements.txt /tmp/requirements.txt
ONBUILD RUN pip install -r /tmp/requirements.txt && rm /tmp/requirements.txt

ONBUILD WORKDIR /app
ONBUILD COPY . /app/
ONBUILD RUN pip install .
