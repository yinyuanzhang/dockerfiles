FROM docker:latest

RUN apk update
RUN apk upgrade
RUN apk add python python-dev py-pip build-base bash git git-subtree openssh-client rsync
RUN pip install docker-compose
