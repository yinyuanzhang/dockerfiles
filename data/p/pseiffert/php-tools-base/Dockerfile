FROM pseiffert/composer
MAINTAINER Paul Seiffert <paul.seiffert@gmail.com>

RUN mkdir -p /opt/tools/bin && cd /opt/tools && composer init
ENV COMPOSER_BIN_DIR /opt/tools/bin

ENTRYPOINT /bin/bash
CMD ['--']
