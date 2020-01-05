FROM naonak/docker-apache-php7
MAINTAINER Fabien EVAIN <fevain@rmn.com>

## Phalcon

# Phalcon version
ENV PHALCON_VERSION 3.0.1

## Install Phalcon PHP extension
RUN cd /tmp \
    && git clone -b v${PHALCON_VERSION} --single-branch --depth 1 git://github.com/phalcon/cphalcon.git \
    && cd cphalcon/build \
    && ./install \
    && rm -rf /tmp/cphalcon/
RUN docker-php-ext-enable phalcon

## Install Phalcon Devtools
RUN git clone  -b v${PHALCON_VERSION} --single-branch --depth 1 git://github.com/phalcon/phalcon-devtools.git /usr/local/lib/phalcon-devtools \
    && ln -s /usr/local/lib/phalcon-devtools/phalcon.php /usr/bin/phalcon \
    && chmod ugo+x /usr/bin/phalcon

## Finalize

CMD ["apache2-foreground"]