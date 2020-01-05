FROM node:latest

RUN apt-get update \
	&& curl -O https://bootstrap.pypa.io/get-pip.py \
	&& apt-get install python-pip -y \
	&& pip install awscli