FROM ruby:latest

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y pdftk

RUN gem install bundler

ENV APP_PATH=/opt

WORKDIR ${APP_PATH}

COPY pdf-filler pdf-filler

WORKDIR ${APP_PATH}/pdf-filler

RUN bundle install

EXPOSE 4567/tcp

ENTRYPOINT [ "ruby", "app.rb" ]
