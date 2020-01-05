FROM python:3.7-alpine
MAINTAINER Erignoux Laurent "laurent.erignoux@ubisoft.com"

## Adding Perforce to the container ##
RUN apk update && apk add --no-cache bash curl git python python-dev py-pip openssl openssl-dev build-base

ADD bin/lib-x64.tgz /

ENV VISUAL=vi
ENV P4_VERSION 16.2

RUN curl -sSL -O http://cdist2.perforce.com/perforce/r${P4_VERSION}/bin.linux26x86_64/p4 && mv p4 /usr/bin/p4 && chmod +x /usr/bin/p4

RUN pip install --upgrade pip p4python

## End perforce requirements ##

COPY . /app
WORKDIR /app

CMD ["python"]
