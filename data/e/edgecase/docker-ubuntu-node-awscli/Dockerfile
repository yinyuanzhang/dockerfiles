FROM ubuntu:14.04
MAINTAINER Lee Goolsbee "lee@edgecase.io"

ENV DEBIAN_FRONTEND=noninteractive

# Update packages
RUN apt-get update -y && apt-get upgrade -y

# Install some packages we need
RUN apt-get install -y build-essential git curl python jq

# Install latest version of pip
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py

# Install Node.JS
RUN cd /usr/local && curl http://nodejs.org/dist/v8.12.0/node-v8.12.0-linux-x64.tar.gz | tar --strip-components=1 -zxf- && cd
RUN npm -g update npm

# Install AWS CLI
RUN pip install awscli awsebcli

# Make sure we land in a shell
CMD ["/bin/bash"]
