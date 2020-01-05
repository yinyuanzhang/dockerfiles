FROM php:7.0-cli-alpine

RUN apk add gcc make libffi-dev musl-dev openssl-dev python3 python3-dev

RUN apk add zip && apk add openssh && apk add rsync 

RUN pip3 install --upgrade pip

RUN pip3 install awscli && \
    pip3 install ansible && \
    pip3 install dump-env

RUN apk add --no-cache libpng libpng-dev && docker-php-ext-install gd

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer 

RUN apk del libpng-dev libffi-dev musl-dev openssl-dev python3-dev

CMD ["/bin/sh"]
