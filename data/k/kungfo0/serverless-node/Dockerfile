FROM node:6.10-slim

RUN apt-get -qq update
RUN apt-get -qq install -y python-pip jq
RUN pip -q install awscli
RUN npm --silent --quiet --no-progress install serverless -g
