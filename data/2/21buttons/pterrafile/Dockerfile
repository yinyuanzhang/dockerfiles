FROM python:2.7-alpine
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /
ADD setup /tmp
RUN apk add git \
    openssh-client \
     make \
 && pip install -r /requirements.txt \
 && pip install -e /tmp \
 && rm /requirements.txt \
 && rm -rf /tmp/setup \
 && mkdir -p /app
WORKDIR /app
