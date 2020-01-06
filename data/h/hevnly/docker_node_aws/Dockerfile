# our base image
FROM node:alpine

# team
MAINTAINER Chris Knight <https://github.com/devfubar>
MAINTAINER Kostas Kapenekakis <https://github.com/ultim8k>

# install bash git ssh zip unzip curl less python3
RUN apk add --update --no-cache bash git openssh zip unzip curl less python3

# set default python version
RUN ln -s /usr/bin/python3 /usr/bin/python

# install grunt and bower
RUN npm install -g grunt-cli
RUN npm install -g --allow-root bower

# config bower
RUN echo '{ "allow_root": true }' > /root/.bowerrc

# install aws sdk
WORKDIR /tmp/
RUN \
  curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" && \
  unzip awscli-bundle.zip && \
  ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Clean up temp dir
RUN rm -rf /tmp/*
