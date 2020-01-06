FROM matt9mg/php7.3
MAINTAINER Thiago Pereira Rosa <thiagor@engineer.com>

RUN apt-get update -y \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends php7.3-dev php-pear composer \
    php7.3-bcmath php7.3-ctype php7.3-json php7.3-mbstring php7.3-pdo php7.3-tokenizer php7.3-xml php7.3-zip php7.3-mysql php7.3-mongodb php7.3-memcached php7.3-xdebug
