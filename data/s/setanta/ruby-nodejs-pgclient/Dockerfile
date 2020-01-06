FROM ruby:2.5.3-slim

RUN apt-get update -qq && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2

RUN curl -sSL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -

RUN apt-get update -qq && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    nodejs \
    postgresql-client \
    yarn

RUN gem update

RUN sed -i 's/\(:DoNotReverseLookup *=> *\).*\(,\)/\1true\2/g' \
           /usr/local/lib/ruby/2.5.0/webrick/config.rb

RUN apt-get clean

