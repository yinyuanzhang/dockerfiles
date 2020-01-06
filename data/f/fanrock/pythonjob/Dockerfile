# if you change this file, rebuild it like this:
# $> docker build -t fanrock/pythonjob:0.3.4 .
#
# then upload to dockerhub like this
# $> docker push fanrock/pythonjob:0.3.4
#
# also update the docker_release.sh and docker_testrun.sh scripts
# to use the new version that you just built and uploaded


# start with official python/alpine base
FROM python:2.7.15-alpine3.7

# start with iron.io's python-2.7 base
# FROM iron/python:2-dev

# update packages
RUN apk update && apk upgrade

# install system-level package dependencies
RUN apk add gcc
RUN apk add alpine-sdk
RUN apk add libxml2-dev
RUN apk add libxslt-dev
RUN apk add musl-dev
RUN apk add python-dev
RUN apk add libffi-dev
RUN apk add postgresql-client
RUN apk add postgresql-dev

# install python-specific requirements
ADD . /worker
WORKDIR /worker
RUN pip install -r requirements.txt

# clear the cache
RUN rm -rf /var/cache/*
