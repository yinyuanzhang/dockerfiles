FROM circleci/php:7.3-apache-node-browsers

USER root

RUN apt-get update && sudo apt-get -y install libpng-dev mariadb-client xvfb ; \
  docker-php-ext-install gd mbstring mysqli pdo pdo_mysql ; \
  \
  npm install -g gulp-cli \
  \
  apt-get clean --yes && \
  rm -rf \
    /tmp/* \
    /var/lib/apt/lists/* \
    /var/tmp/* ;

USER circleci

CMD ["/bin/sh"]
