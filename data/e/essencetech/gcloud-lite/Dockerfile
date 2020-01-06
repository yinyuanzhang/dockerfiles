FROM docker:stable-dind 
LABEL maintainer="michel.laporte@essenceglobal.com"
LABEL version="1.1"
RUN apk update && apk add --no-cache bash git gcc musl-dev python-dev build-base util-linux libffi-dev openssl-dev openssl grep py2-pip curl || true
RUN pip install docker-compose
RUN sed -i s/"DEFAULT_POOLSIZE = 10"/"DEFAULT_POOLSIZE = 1000"/g /usr/lib/python2.7/site-packages/requests/adapters.py && \
    sed -i s/"DEFAULT_POOLSIZE = 10"/"DEFAULT_POOLSIZE = 1000"/g /usr/lib/python2.7/site-packages/pip/_vendor/requests/adapters.py && \
    curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin
