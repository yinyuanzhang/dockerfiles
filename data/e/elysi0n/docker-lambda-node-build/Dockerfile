FROM node:7

MAINTAINER Trevor <trevor@elysion.io>

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install -y yarn

# Install awscli
RUN apt-get install -y python-dev python-pip

# Install jq
RUN apt-get install -y jq

RUN pip install awscli