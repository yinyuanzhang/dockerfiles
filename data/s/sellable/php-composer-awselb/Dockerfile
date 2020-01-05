FROM alpine:latest
MAINTAINER Mohamad Ali <mohamad@sellable.com.au>

RUN apk -v add \
	git \
	curl \
	python

RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    pip install -U setuptools

RUN pip install --upgrade awsebcli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*

RUN rm -rf ~/.aws

VOLUME ["/root/.aws"]