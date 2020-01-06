FROM circleci/ruby:2.6.5-node

ENV URL "https://omnibus-aptible-toolbelt.s3.amazonaws.com/aptible/omnibus-aptible-toolbelt/master/176/pkg/aptible-toolbelt_0.16.1%2B20180730142012%7Edebian.8.10-1_amd64.deb"

USER root

RUN apt-get update \
    && apt-get install -y curl \
    && curl -o aptible-cli.deb "$URL" \
    && dpkg -i aptible-cli.deb \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f aptible-cli.deb

RUN curl -sL https://sentry.io/get-cli/ | bash
