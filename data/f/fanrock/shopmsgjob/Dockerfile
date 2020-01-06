# if you change this file, rebuild it like this:
# $> docker build -t fanrock/shopmsgjob:{version} .
#
# then upload to dockerhub like this
# $> docker push fanrock/shopmsgjob:{version}
#

# start with official python/alpine base
FROM python:3.7.3-alpine3.8

# update packages
RUN apk update && apk upgrade

# install system-level package dependencies
RUN apk add gcc
RUN apk add alpine-sdk
RUN apk add libxml2-dev
RUN apk add libxslt-dev
RUN apk add musl-dev
RUN apk add python3-dev
RUN apk add libffi-dev
RUN apk add postgresql-client
RUN apk add postgresql-dev

# install python-specific requirements
ADD . /worker
WORKDIR /worker
RUN pip install -r requirements.txt

# clear the cache
RUN rm -rf /var/cache/*