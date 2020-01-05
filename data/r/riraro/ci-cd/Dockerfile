FROM python:3.6-alpine3.7

RUN apk add --no-cache curl git openssh

COPY requirements.txt .

RUN pip3 --no-cache-dir install -r requirements.txt --upgrade

RUN rm -f requirements.txt

RUN pip3 --no-cache-dir install docker-compose

ENV PATH "~/.local/bin:${PATH}"

ENTRYPOINT ["/bin/sh"]
