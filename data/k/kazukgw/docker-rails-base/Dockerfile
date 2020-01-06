FROM kazukgw/docker-ruby:2.2.0

MAINTAINER Kazuya Kagawa "kazukgw@gmail.com"

RUN apt-get update && \
      apt-get install -y language-pack-ja --no-install-recommends && \
      rm -rf /var/lib/apt/lists/*
RUN update-locale LANG=ja_JP.UTF-8
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8

RUN apt-get update && \
      apt-get install -y nodejs --no-install-recommends && \
      rm -rf /var/lib/apt/lists/*

RUN apt-get update && \ 
      apt-get install -y \
        imagemagick \
        mysql-client \
        libmysqld-dev \ 
        postgresql-client \
        libpq-dev \
        sqlite3 --no-install-recommends && \
      rm -rf /var/lib/apt/lists/*

##### 
RUN ln -s /usr/bin/nodejs /usr/bin/node

# install npm && bower
RUN curl -L https://npmjs.com/install.sh | sh
RUN npm install -g bower

ENV RAILS_VERSION 4.2.0

RUN gem install rails --version "$RAILS_VERSION"

RUN gem install \
pry \
annotate \
pry-rails \
pry-doc \
pry-stack_explorer \
pry-byebug \
better_errors \
rack-mini-profiler \
timecop \
rails_best_practices \
mysql2 \
minitest-rails \
factory_girl_rails \
database_cleaner \
mocha \
bullet \
yajl-ruby \
devise \
bootstrap-sass \
activerecord-import \
haml-rails \
parallel \
nokogiri \
will_paginate \
bootstrap-will_paginate \
coffee-script \
coffee-rails \
commonjs \
responders \
unf_ext \
unf \
domain_name \
email_validator \
http-cookie \
net-http-digest_auth \
net-http-persistent \
ntlm-http \
webrobots \
mechanize \
sprockets-rails \
i18n_generators \
jbuilder \
jquery-rails \
less \
less-rails \
libv8 \
pg \
rails_serve_static_assets \
rails_stdout_logging \
rails_12factor \
ref \
sass-rails \
sdoc \
spring \
therubyracer \
twitter-bootstrap-rails \
uglifier \
web-console

