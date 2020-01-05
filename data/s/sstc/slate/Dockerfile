# https://github.com/lord/slate/wiki/Docker#alternative-approach-with-ruby-25-alpine
FROM ruby:2.5-alpine

RUN apk update \
  && apk add coreutils git make g++ nodejs

RUN git clone https://github.com/lord/slate app

WORKDIR /app

RUN mv source source_orig \
  && bundle install

CMD [ \
  "cp -nr source_orig/* source" \
  "exec bundle exec middleman server --watcher-force-polling" \
]

VOLUME [ \
  "/app/source" \
  "/app/build" \
]
EXPOSE 4567
