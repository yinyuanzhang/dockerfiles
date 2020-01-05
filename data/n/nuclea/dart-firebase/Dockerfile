FROM google/dart:latest

LABEL description='Docker image that contains latest dart and firebase-tools CLI'
LABEL version="1.0.1"
LABEL firebase-version='7.11.0'
LABEL dart-version="2.7.0"

ENV PATH="/root/.pub-cache/bin:${PATH}"

RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update && apt-get install -y nodejs yarn
RUN npm i -g firebase-tools
RUN pub global activate webdev
