FROM python:3.7-alpine
RUN apk add --no-cache --update bash curl openssl ca-certificates jq vim
RUN pip install --upgrade pip
COPY assets/ /opt/resource/
RUN pip install -r /opt/resource/requirements.txt
RUN chmod +x /opt/resource/*
