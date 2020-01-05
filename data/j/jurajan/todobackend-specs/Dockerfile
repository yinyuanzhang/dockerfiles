FROM ubuntu:trusty
LABEL maintainer="Juraj"

ENV TERM xterm-256color

RUN apt-get update && \
    apt-get install curl -y && \
	curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \
	apt-get install -y nodejs


COPY . /app
WORKDIR /app

RUN npm install -g mocha && \
    npm install -g mocha-jenkins-reporter && \
    npm install

ENTRYPOINT ["mocha"]
