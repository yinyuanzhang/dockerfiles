FROM ubuntu:latest

ENV	DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    git \
    php-cli \
    php-mbstring \
    php-gd \
    php-curl \
    php-xml \
    php-zip \
    php-mysql \
    curl \
    ca-certificates \
    openssh-client \
    sshpass \
    mysql-client \
    jq

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

RUN composer global require --dev lucatume/wp-browser

RUN ln -s /root/.composer/vendor/codeception/codeception/codecept /usr/local/bin/codecept

RUN curl https://s3.amazonaws.com/lambda-tunnel/LT_Linux.zip --output /usr/local/bin/LT
RUN chmod +x /usr/local/bin/LT

COPY wait_services.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait_services.sh

RUN rm -rf /var/lib/apt/lists/*
