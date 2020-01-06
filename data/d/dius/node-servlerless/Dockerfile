FROM mhart/alpine-node:8.11.3

RUN apk update && \
    apk add \
    curl \
    python

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py --user && \
    /root/.local/bin/pip install awscli --upgrade --user

RUN npm install -g serverless

ENV PATH "$PATH:/root/.local/bin"