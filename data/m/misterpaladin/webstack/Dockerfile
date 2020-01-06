FROM ubuntu:16.04
LABEL maintainer="Min De Sik <e.v.min@icloud.com>"

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y sudo nano wget curl openssh-client zip apt-transport-https

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt-get update -y
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install software-properties-common
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update && \
    apt-get install -y language-pack-en-base &&\
    export LC_ALL=en_US.UTF-8 && \
    export LANG=en_US.UTF-8
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository -y ppa:ondrej/php
RUN apt-get update -y
RUN apt-get install -y --allow-unauthenticated nginx php7.2-fpm php7.2-mbstring php7.2-memcached php7.2-gd php7.2-sqlite php7.2-json php7.2-mysqlnd php7.2-pdo-pgsql php7.2-curl php7.2-xml php7.2-bcmath php7.2-imagick ruby ruby-dev make gcc build-essential
RUN apt-get install -y --allow-unauthenticated nginx php7.1-fpm php7.1-mbstring php7.1-memcached php7.1-gd php7.1-sqlite php7.1-json php7.1-mysqlnd php7.1-pdo-pgsql php7.1-curl php7.1-xml php7.1-bcmath php7.1-imagick
RUN apt-get install -y --allow-unauthenticated nginx php7.0-fpm php7.0-mbstring php7.0-memcached php7.0-gd php7.0-sqlite php7.0-json php7.0-mysqlnd php7.0-pdo-pgsql php7.0-curl php7.0-xml php7.0-bcmath php7.0-imagick
RUN apt-get install -y --allow-unauthenticated nginx php5.6-fpm php5.6-mbstring php5.6-memcached php5.6-gd php5.6-sqlite php5.6-json php5.6-mysqlnd php5.6-pdo-pgsql php5.6-curl php5.6-xml php5.6-bcmath php5.6-imagick php5.6-mcrypt
RUN gem install jekyll bundler

RUN echo "www-data ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer
RUN rm composer-setup.php
RUN wget -O phpunit https://phar.phpunit.de/phpunit-7.phar && mv phpunit /usr/local/bin && chmod +x /usr/local/bin/phpunit

WORKDIR /srv

RUN apt-get install -y git
RUN wget https://nodejs.org/dist/v10.15.3/node-v10.15.3-linux-x64.tar.gz
RUN tar -C /usr/local --strip-components 1 -xzf node-v10.15.3-linux-x64.tar.gz
RUN rm node-v10.15.3-linux-x64.tar.gz
RUN apt-get install yarn -y --no-install-recommends

COPY ./scripts/serve.sh /usr/local/bin/serve
RUN chmod +x /usr/local/bin/serve

EXPOSE 80 8000 443
CMD sh /srv/startup.sh; service nginx start && service php5.6-fpm start && service php7.0-fpm start && service php7.1-fpm start && service php7.2-fpm start && tail -F /var/log/nginx/*