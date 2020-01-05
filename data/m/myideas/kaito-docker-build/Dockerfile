FROM ubuntu

LABEL maintainer="it@kaito.tech"
RUN apt-get update && \
    apt-get install -y git curl python-pip nodejs npm zip && \
    ln -s /usr/bin/nodejs /usr/bin/node && \
    pip install --upgrade pip && \
    pip install awscli --upgrade --user

ENV PATH "$PATH:/root/.local/bin"



