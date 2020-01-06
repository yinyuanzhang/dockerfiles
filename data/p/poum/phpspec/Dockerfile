# PHPSpec Docker Container 
FROM composer/composer:alpine 
MAINTAINER Philippe Poumaroux <poum@cpan.org>

ENV VERSION=3.2.2

# Goto temporary directory 
WORKDIR /tmp

# Run composer and phpspec installation.
RUN composer selfupdate && \
    composer require "phpspec/phpspec:~$VERSION" --dev && \
    ln -s /tmp/vendor/bin/phpspec /usr/local/bin/phpspec

# Set up the application directory. 
VOLUME ["/app"]
WORKDIR /app

# Set up the command arguments.
ENTRYPOINT ["/usr/local/bin/phpspec"]
CMD ["--help"]
