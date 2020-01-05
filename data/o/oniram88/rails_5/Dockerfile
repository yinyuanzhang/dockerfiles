FROM ruby:2.4.1-slim-jessie

RUN apt-get update -qq && apt-get install -y -qq curl build-essential \
    imagemagick openssh-client \
    libmagickwand-dev git libsqlite3-dev
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash -
# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
# Install packages
RUN apt-get update -qq && apt-get install -y -qq  nodejs yarn
RUN gem install bundler --no-ri --no-rdoc
