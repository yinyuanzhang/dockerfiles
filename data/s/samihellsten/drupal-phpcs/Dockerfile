FROM willhallonline/composer:php-7.2
LABEL maintainer="dropa@dropa.net"

# Install Drupal Coding Standards
RUN composer global require drupal/coder:8.x-3.x-dev

# Set Drupal as default CodeSniffer Standard
RUN phpcs --config-set installed_paths /root/.composer/vendor/drupal/coder/coder_sniffer/ \
    && phpcs --config-set default_standard Drupal,DrupalPractice

WORKDIR /app

CMD ["phpcs"]
CMD ["phpcbf"]
