FROM node

RUN apt-get update -y \
    && apt-get install -y python-pip \
    && pip install awscli \
    && rm -rf /var/lib/apt/lists/* /root/.cache/*

USER node
