FROM ubuntu:14.04

RUN apt update \
 && apt install -y software-properties-common \
 && apt-add-repository ppa:brightbox/ruby-ng \
 && apt update \
 && apt install -y ruby2.4 ruby2.4-dev \
 && apt install -y pkg-config build-essential nodejs git libxml2-dev libxslt-dev \
 && gem2.4 install --no-ri --no-rdoc bundler \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists

COPY . /slate
WORKDIR /slate

RUN bundle config build.nokogiri --use-system-libraries \
 && bundle install
RUN rm -rf /slate/source

ONBUILD COPY . /slate/source
ONBUILD RUN bundle exec middleman build --clean
