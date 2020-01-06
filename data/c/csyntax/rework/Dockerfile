FROM ubuntu:16.04

LABEL maintainer="Ivan Ivanov csyntax@outlook.com"

ENV RAILS_ENV production

RUN apt-get update -y && apt-get install --fix-missing --no-install-recommends -y git-core \
    curl \
    wget \
    zlib1g-dev \
    build-essential \
    libssl-dev \
    libreadline-dev \
    libyaml-dev \
    libsqlite3-dev \ 
    sqlite3 \
    libxml2-dev \
    libxslt1-dev \
    libcurl4-openssl-dev \
    libffi-dev \
    #ruby \
    #ruby-dev\
    git

RUN cd && \
    wget http://ftp.ruby-lang.org/pub/ruby/2.3/ruby-2.3.7.tar.gz && \
    tar -xzvf ruby-2.3.7.tar.gz && \
    cd ruby-2.3.7 && \
    ./configure && \
    make && make install && \
    ruby -v && cd .. && \
    curl -sL https://deb.nodesource.com/setup_8.x | bash && \
    apt-get install --fix-missing --no-install-recommends -y nodejs

RUN gem install bundler

RUN mkdir wealthoz
WORKDIR wealthoz

COPY . /wealthoz

RUN bundle install --path vendor/bundle --without development
RUN bundle exec rake assets:precompile
RUN bundle exec rake db:migrate
RUN bundle exec rake db:seed

CMD bundle exec puma -C config/puma.rb

EXPOSE 5000
