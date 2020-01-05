# The base image is node 9 alpine
FROM node:9-alpine

# Author: Roy Evangelista
MAINTAINER Roy Evangelista <royevangelista@gmail.com>

# Install new packages
RUN apk add --update build-base openssl-dev git openssh-client

# Copied from base image
CMD ["node"]
