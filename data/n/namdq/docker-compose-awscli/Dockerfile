FROM docker:stable

LABEL maintainer="Nam Dau <namdq.nu@gmail.com>"

RUN apk update -q && apk add --no-cache curl jq python3 py-pip bash rsync openssh openssh-client
RUN apk add 
RUN pip3 install docker-compose
RUN pip3 install awscli
RUN pip3 install awsebcli --upgrade --user