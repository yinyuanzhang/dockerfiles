FROM ubuntu:16.04

###############################################################################
# General dependencies
###############################################################################
RUN apt-get update
RUN apt-get install -y \
    curl \
    git \
    jq \
    python3 \
    python3-pip \
    screen \
    wget \
    sudo \
    zip


###############################################################################
# SERVERLESS
###############################################################################
RUN curl -sL https://deb.nodesource.com/setup_11.x | bash -
RUN apt-get install -y nodejs
RUN npm install -g serverless@1.39.1


###############################################################################
# AWS
###############################################################################
RUN pip3 install awscli==1.16.144
RUN mkdir /root/.aws


###############################################################################
# Pip3 dependencies
###############################################################################
ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
