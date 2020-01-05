FROM ruby:2.6.5-alpine3.10

LABEL "com.github.actions.name"="RuboCop"
LABEL "com.github.actions.description"="RuboCop is a Ruby static code analyzer and code formatter."
LABEL "com.github.actions.icon"="flag"
LABEL "com.github.actions.color"="red"

RUN apk add --no-cache \
  build-base=~0.5 \
  git

RUN addgroup -S rubocop && \
  adduser -S -g rubocop rubocop

RUN gem install rubocop --no-document

COPY entrypoint.sh /entrypoint.sh

COPY rubocop-problem-matcher.json /rubocop-problem-matcher.json

ENTRYPOINT ["/entrypoint.sh"]