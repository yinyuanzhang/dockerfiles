# Behat Docker Container 
FROM composer/composer:alpine 
LABEL maintainer "Philippe Poumaroux <poum@cpan.org>"

ENV VERSION_BEHAT=3.4

# Goto temporary directory
WORKDIR /tmp

# Run composer and phpspec installation. 
RUN composer selfupdate && \
  composer require \
    behat/behat:~$VERSION_BEHAT \
    behat/mink \
    behat/mink-extension \
    laracasts/behat-laravel-extension \
    --dev && \
  ln -s /tmp/vendor/bin/behat /usr/local/bin/behat

# Set up the application directory. 
VOLUME ["/app"]
WORKDIR /app

# Set up the command arguments. 
ENTRYPOINT ["/usr/local/bin/behat"]
CMD ["--help"]
