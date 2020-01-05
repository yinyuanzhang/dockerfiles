FROM jenkins/ssh-slave

# Install selected extensions and other stuff
RUN apt-get update \
    && apt-get -y --no-install-recommends install \
    php7.2-cli \
    php-xdebug \ 
    composer \
    phpunit \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
