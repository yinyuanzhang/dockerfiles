FROM python:2.7-slim

RUN set -ex \
  && apt-get update \
  && apt-get install -qq -y curl \
  && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
  && apt-get install -qq -y nodejs \
  && apt-get clean
