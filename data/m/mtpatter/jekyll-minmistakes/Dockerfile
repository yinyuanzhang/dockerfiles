# Version: 0.0.2
FROM ubuntu
MAINTAINER Maria Patterson "maria.t.patterson@gmail.com"
ENV REFRESHED_AT 2017-04-27

RUN apt-get update -y
RUN apt-get install -y ruby ruby-dev
RUN apt-get install -y make gcc libgmp-dev
RUN apt-get install -y nodejs
RUN apt-get install -y zlib1g-dev liblzma-dev
#RUN gem install rubygems-update
#RUN update_rubygems

RUN gem install listen
RUN gem install bundler -v '1.17.3'

EXPOSE 4000

COPY Gemfile* /srv/jekyll/
WORKDIR /srv/jekyll/

RUN bundle update json
RUN bundle install
CMD bundle exec jekyll serve --host=0.0.0.0 --force_polling --watch
