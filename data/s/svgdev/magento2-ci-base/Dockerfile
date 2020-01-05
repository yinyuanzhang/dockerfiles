FROM php:7.0-fpm

# apt deps
RUN apt-get update && apt-get install -y libfreetype6-dev git libjpeg62-turbo-dev unzip cron mysql-client zip libxslt1-dev libmcrypt-dev libicu-dev gzip jq python-pip curl apt-transport-https

# php deps

RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install bcmath gd intl mbstring mcrypt opcache pdo_mysql soap xsl zip

#composer

RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# docker-compose

RUN curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose

#kubectl

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl
RUN chmod +x ./kubectl
RUN mv ./kubectl /usr/local/bin/kubectl

#aws cli

RUN pip install awscli

# helm

RUN curl -LO https://git.io/get_helm.sh
RUN chmod 700 get_helm.sh
RUN ./get_helm.sh
