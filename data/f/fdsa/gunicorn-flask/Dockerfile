FROM python:3.6-alpine

RUN apk add --no-cache build-base python3-dev
COPY req.txt /tmp/
RUN pip install -r /tmp/req.txt && rm /tmp/req.txt
