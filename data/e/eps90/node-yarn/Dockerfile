FROM ubuntu:16.04
WORKDIR /root

RUN apt-get update && apt-get install -y locales curl software-properties-common ssh build-essential git

RUN mkdir .ssh
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV CI 1

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y yarn

RUN npm install -g gulp-cli

RUN npm --version
RUN yarn --version
RUN gulp --version
