FROM docker:latest

RUN apk update \
 && apk upgrade \
 && apk add --no-cache curl jq python py-pip \
 && apk add --no-cache bash git openssh \
 && apk add --update nodejs nodejs-npm yarn \
 && pip install --upgrade pip \
 && pip install awscli 

