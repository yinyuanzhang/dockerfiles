FROM golang:1.12-stretch

MAINTAINER Maximilian Schmitt

RUN apt-get update \
	&& apt-get install -y jq python-pip curl apt-transport-https \
	&& apt-get clean \
	&& pip install awscli
