FROM alpine:3.10
MAINTAINER Stefano Marinelli <stefano@dragas.it>

RUN apk add --no-cache git python py-jinja2 py-paramiko && git clone https://github.com/PackeTsar/checkmyip.git && apk del --no-cache git

EXPOSE 22
EXPOSE 23
EXPOSE 80

ENTRYPOINT /checkmyip/checkmyip.py
