#
# isodevnet/iso-docker-cicd-image
#
# Based on alpine + awsebcli, etc
#

# Docker file to run AWS EB CLI tools.
FROM alpine:3.10

ARG EBS_VERSION=3.15.3

# Expose credentials volume
RUN mkdir ~/.aws

RUN apk --no-cache --update add bash git curl zip make python py-pip

RUN pip install --upgrade pip awsebcli==$EBS_VERSION

