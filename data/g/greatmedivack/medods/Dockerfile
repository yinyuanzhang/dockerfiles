FROM ruby:2.4.2

RUN apt-get update
RUN apt-get install -y curl git sudo imagemagick
RUN apt-get install  -y --no-install-recommends apt-utils
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update
RUN apt-get install yarn -y

RUN mkdir /medods
WORKDIR /medods

COPY . /medods
COPY ./config/database.yml.docker /medods/config/database.yml
COPY ./config/cable.yml.docker /medods/config/cable.yml

RUN bundle
RUN yarn
RUN bundle exec rake assets:precompile RAILS_ENV=production