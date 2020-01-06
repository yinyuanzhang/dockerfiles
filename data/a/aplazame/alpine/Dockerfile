
FROM node:10-alpine

RUN apk add --update \
	bash \
	git \
	curl \
	rsync \
	make \
	ca-certificates \
    python3

RUN rm -rf /var/cache/apk/*

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py; \
	python3 get-pip.py; \
	rm get-pip.py

RUN pip install awscli

ENTRYPOINT /bin/bash