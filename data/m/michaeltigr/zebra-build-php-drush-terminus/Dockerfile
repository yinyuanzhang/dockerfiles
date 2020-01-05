FROM michaeltigr/zebra-build-php-drush:latest

LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"

USER root

ENV TERMINUS_VERSION=2.1.0
RUN wget -O /usr/local/bin/terminus https://github.com/pantheon-systems/terminus/releases/download/${TERMINUS_VERSION}/terminus.phar \
  && chmod +x /usr/local/bin/terminus
