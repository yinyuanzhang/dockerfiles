FROM alpine:edge

WORKDIR /tmp

RUN apk --no-cache --repository http://dl-cdn.alpinelinux.org/alpine/v3.5/community add \
        bash \
        ca-certificates \
        git \
        curl \
        unzip \
        php5-cli \
        php5-xml \
        php5-zip \
        php5-xmlreader \
        php5-zlib \
        php5-opcache \
        php5-mcrypt \
        php5-openssl \
        php5-curl \
        php5-json \
        php5-dom \
        php5-phar \
        php5-bcmath \
        php5-pdo \
        php5-pdo_pgsql \
        php5-pdo_sqlite \
        php5-pdo_mysql \
        php5-soap \
        php5-pcntl \
        php5-ctype \
        jq \
        php5-imap \

    && ln -s /usr/bin/php5 /usr/bin/php \
    && php -r "copy('https://pear.php.net/go-pear.phar', 'go-pear.phar');" \
    && php go-pear.phar \
    && php -r "unlink('go-pear.phar');" \
    && php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
    && php composer-setup.php --install-dir=/usr/bin --filename=composer \
    && php -r "unlink('composer-setup.php');" \
    && composer require "phpunit/phpunit:~5.7.5" --prefer-source --no-interaction \
    && composer require "phpunit/php-invoker" --prefer-source --no-interaction \
    && ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit

# install python3
RUN apk add --update --no-cache python3

# set default python version
RUN ln -s /usr/bin/python3 /usr/bin/python

# install aws cli
ADD https://s3.amazonaws.com/aws-cli/awscli-bundle.zip /tmp/awscli-bundle.zip
RUN unzip /tmp/awscli-bundle.zip -d /tmp/ && \
/tmp/awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
rm -rf /tmp/awscli-bundle.zip /tmp/awscli-bundle

VOLUME ["/app"]
WORKDIR /app

ENTRYPOINT ["/usr/local/bin/phpunit"]
CMD ["--help"]
