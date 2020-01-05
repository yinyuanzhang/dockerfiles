FROM ruby:2.5.1-stretch

LABEL maintainer="himuhasib@gmail.com"

RUN apt-get update && apt-get install -y gnupg
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -E -
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update && apt-get install -y \
        nodejs \
        openssh-client \
        rsync \
        tar \
        yarn \
        zip

RUN gem install dpl

RUN apt-get remove -y gnupg && apt-get autoremove -y && apt-get clean -y
