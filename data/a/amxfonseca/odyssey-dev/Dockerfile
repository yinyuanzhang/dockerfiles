FROM debian:jessie-slim
LABEL maintainer "André Fonseca <andre@strangelovel.nl>"

RUN apt-get update -q \
  && apt-get -yq --no-install-recommends install \
    php5-cli php5-curl php5-mongo php5-gd php5-mcrypt php5-imagick \
    ca-certificates \
  && rm -rf /var/lib/apt/lists/*

COPY 90-custom.ini /etc/php5/cli/conf.d/
COPY server.php /server.php

STOPSIGNAL SIGINT
ENTRYPOINT ["php"]
