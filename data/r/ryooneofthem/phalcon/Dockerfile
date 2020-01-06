FROM debian:wheezy

RUN apt-get update && apt-get -y install \
  curl

RUN echo "deb http://packages.dotdeb.org wheezy-php55 all" >> /etc/apt/sources.list && \
    echo "deb-src http://packages.dotdeb.org wheezy-php55 all" >> /etc/apt/sources.list && \
    curl -L https://www.dotdeb.org/dotdeb.gpg -o dotdeb.gpg && \
    apt-key add dotdeb.gpg

RUN apt-get update && apt-get -y install \
  git \
  zip \
  libyaml-dev \
  php5-cli \
  php5-dev \
  php5-fpm \
  libpcre3-dev \
  php-pear \
  gcc \
  make \
  php5-mysqlnd \
  mysql-client \
  php5-curl \
  && cd /usr/local/bin \
  && curl -L https://github.com/jwilder/docker-gen/releases/download/0.3.4/docker-gen-linux-amd64-0.3.4.tar.gz \
  | tar -xzv 

RUN git clone --depth=1 http://github.com/phalcon/cphalcon.git -b 1.2.4 cphalcon \
 && cd cphalcon/build && ./install \
 && pecl install YAML \
 && pecl install redis-2.2.8

RUN echo 'extension=phalcon.so' >> /etc/php5/fpm/conf.d/30-phalcon.ini \
 && echo 'extension=yaml.so' >> /etc/php5/fpm/conf.d/40-yaml.ini \
 && echo 'extension=redis.so' >> /etc/php5/fpm/conf.d/50-redis.ini \ 
 && echo 'date.timezone="Asia/Tokyo"' >> /etc/php5/fpm/conf.d/60-timezone.ini \ 
 && cp -a /etc/php5/fpm/conf.d/*.ini /etc/php5/cli/conf.d/

