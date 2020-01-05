FROM php:7.2-fpm

ARG TIMEZONE="Europe/Paris"

RUN apt-get update && apt-get install -y \
    apt-transport-https \
    openssl \
    libmcrypt-dev \
    git \
    ssh \
    unzip \
    libxml2-dev \
    libxslt-dev \
    zlib1g-dev \
    libicu-dev \
    libxrender1 \
    libfontconfig1 \
    libssl1.0-dev \
    g++ \
    wget \
    sudo \
    locales

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN composer --version

# Set timezone
RUN ln -snf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo ${TIMEZONE} > /etc/timezone
RUN printf '[PHP]\ndate.timezone = "%s"\n', ${TIMEZONE} > /usr/local/etc/php/conf.d/tzone.ini
RUN "date"

# Install extensions
RUN docker-php-ext-install \
            xsl \
            json \
            intl \
            opcache \
            mbstring \
            pdo_mysql \
            sockets \
            zip \
            xsl \
            json


# Install for  wkhtmltopdf
RUN wget "https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz"
ENV DEBIAN_FRONTEND=noninteractive
RUN cd ~
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
       && tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
       && mv wkhtmltox/bin/wkhtmlto* /usr/bin/ \
       && rm -rf wkhtmltox

RUN echo 'alias sf="php bin/console"' >> ~/.bashrc
RUN echo 'alias go="./go.sh"' >> ~/.bashrc
RUN echo 'alias load="sf doctrine:fixtures:load && go"' >> ~/.bashrc
RUN echo 'alias dump="sf doctrine:schema:update --dump-sql"' >> ~/.bashrc
RUN echo 'alias force="sf doctrine:schema:update --force"' >> ~/.bashrc
RUN echo 'alias update="composer update -vvv && chmod 777 -R var/cache && chmod 777 -R vendor"' >> ~/.bashrc
RUN echo 'alias dge="sf doctrine:generate:entities"' >> ~/.bashrc

WORKDIR /var/www/symfony
