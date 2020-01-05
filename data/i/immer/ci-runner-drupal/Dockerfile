FROM ubuntu:16.04

EXPOSE 80

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      php7.0-mcrypt php7.0-mbstring php7.0-xml php7.0-mysql php7.0-opcache php7.0-json \
      php7.0-gd php7.0-curl php7.0-ldap php7.0-mysql php7.0-odbc php7.0-soap php7.0-xsl \
      php7.0-zip php7.0-intl php7.0-cli \
      npm nodejs nodejs-legacy rsync \
      build-essential \
      unzip ruby libffi-dev ruby-dev git-core ssh curl mysql-client \
 && rm -Rf /var/cache/apt/* \
 && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
 && php composer-setup.php \
 && php -r "unlink('composer-setup.php');" \
 && mv composer.phar /usr/local/bin/composer \
 && echo 'export PATH="$PATH:/var/www/vendor/bin"' >> ~/.bashrc \
 && gem install bundler \
 && npm install -g grunt-cli

CMD ["bash"]
