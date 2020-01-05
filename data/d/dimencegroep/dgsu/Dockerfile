FROM debian:9-slim

ENV DEBIAN_FRONTEND noninteractive
ENV DRUPAL_VERSION 8

RUN apt-get update -y
RUN apt-get upgrade -y

RUN apt-get install -y --no-install-recommends apt-utils wget git unzip

# Install MySQL server
RUN echo 'mysql-server mysql-server/root_password password password' | debconf-set-selections && \
    echo 'mysql-server mysql-server/root_password_again password password' | debconf-set-selections && \
    apt-get install -y mysql-client mysql-server

RUN apt-get install -y apt-transport-https lsb-release ca-certificates && \
    wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg && \
    echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/php.list && \
    apt-get update -y

## Install php and nginx
RUN apt-get install -y php7.1-fpm php7.1-mysql php7.1-gd php7.1-mcrypt php7.1-mysql php7.1-curl php7.1-xml nginx curl && \
    rm -rf /var/lib/apt/lists/*

# Install Composer
RUN curl -sS https://getcomposer.org/installer -o composer-setup.php && \
    php composer-setup.php --install-dir=/usr/local/bin --filename=composer

# Install drush
RUN export PATH="$HOME/.composer/vendor/bin:$PATH" && \
    composer global require drush/drush:7.*
RUN useradd -ms /bin/bash gitlab-runner

RUN apt-get update && apt-get upgrade -y
RUN apt-get install openssh-server openssh-client -y

VOLUME ["/var/www/", "/var/lib/mysql/"]

ADD script.sh /root/script.sh
RUN chmod u+x /root/script.sh

ADD comparer /var/www/tmp/comparer

ENTRYPOINT ["/root/script.sh"]
WORKDIR "/var/www/tmp/comparer"
