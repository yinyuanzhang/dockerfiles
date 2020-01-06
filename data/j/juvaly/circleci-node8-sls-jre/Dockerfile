FROM circleci/node:8
MAINTAINER juvaly

USER root

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get autoremove -y && \
    apt-get upgrade -y && \
    apt-get install -y default-jre

RUN apt-get install -y python-pip && \
    pip install awscli

RUN npm install -g serverless mocha babel-cli

USER circleci

CMD [ "node" ]
