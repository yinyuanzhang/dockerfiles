# Ubuntu Xenial = 16.04
FROM ubuntu:xenial

LABEL vendor="John Housser"
LABEL maintainer="John Housser"
LABEL com.arcteryx.version="0.0.1"
LABEL com.arcteryx.release-date="2018-09-24"

RUN apt-get update && apt-get install -y \
  curl \
  git \
  zip \
  python-pip

# Install NodeJS v8
# https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs

RUN pip install -U awscli

RUN npm install -g gatsby-cli