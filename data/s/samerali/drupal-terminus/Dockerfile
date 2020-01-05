FROM wodby/drupal-php:7.2

USER wodby
ENV WODBY_APP_NAME=terminus
RUN cd /tmp && curl -O "https://raw.githubusercontent.com/pantheon-systems/terminus-installer/master/builds/installer.phar" && php installer.phar install --install-version=2.0.0 --install-dir=/home/wodby
