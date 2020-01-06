FROM ruby:2.6.4-stretch

RUN gem install rails

RUN apt-get update && \
    apt-get install -y build-essential nodejs mysql-client

RUN apt-get install -y curl apt-transport-https wget && \
    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list &&\
    apt-get update && apt-get install -y yarn    

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
    apt-get install nodejs

COPY Gemfile /Gemfile
COPY Gemfile.lock /Gemfile.lock
RUN bundle install

