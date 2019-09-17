FROM michaeltigr/zebra-php-base:latest

LABEL maintainer "Michael Molchanov <mmolchanov@adyax.com>"

USER root

# Set the Drush version.
ENV DRUSH_VERSION 8.3.0

# Install Drush 8 with the phar file.
RUN curl -fsSL -o /usr/local/bin/drush "https://github.com/drush-ops/drush/releases/download/$DRUSH_VERSION/drush.phar" && \
  chmod +x /usr/local/bin/drush

# Test your install.
RUN drush core-status
