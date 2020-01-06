FROM python:3.7.2-alpine

MAINTAINER michael.barry@intlfcstone.com

RUN apk add git
RUN mkdir oxidized-tooling
RUN pip install pynetbox
ADD . /oxidized-tmp
RUN git clone https://github.com/barryCrunch/oxidized-tooling.git
RUN cp /oxidized-tmp/entrypoint.sh /oxidized-tooling/
WORKDIR /oxidized-tooling

RUN chmod +x entrypoint.sh
