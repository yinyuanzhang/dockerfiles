FROM ubuntu:12.04

RUN apt-get update && \
    apt-get install --yes curl && \
    curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
    apt-get install --yes nodejs git && \
    npm install -g gulp bower mocha nodemon

