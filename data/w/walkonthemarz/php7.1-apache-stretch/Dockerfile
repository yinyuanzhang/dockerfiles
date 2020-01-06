FROM php:7.1-apache-stretch

MAINTAINER walkonthemarz@gmail.com

RUN apt update \
      && apt upgrade -y \
      && apt install -y wget pdftk \
      && a2enmod rewrite \
      && pecl install redis-4.1.1 && docker-php-ext-enable redis \
      && apt install -y libmcrypt-dev \
      && apt install -y mysql-client \
      #&& docker-php-ext-install json \
      #&& docker-php-ext-install hash \
      #&& docker-php-ext-install curl \
      && docker-php-ext-install mbstring \
      && docker-php-ext-install pdo_mysql \
      && docker-php-ext-install mysqli \
      && docker-php-ext-install mcrypt \
      #&& docker-php-ext-install iconv \
      #&& docker-php-ext-install xml
      #&& docker-php-ext-install openssl \
      && wget https://nodejs.org/dist/v8.12.0/node-v8.12.0-linux-x64.tar.xz -O /opt/node-v8.12.0-linux-x64.tar.xz \
      && tar -xvf /opt/node-v8.12.0-linux-x64.tar.xz -C /opt && rm -f /opt/node-v8.12.0-linux-x64.tar.xz 

#COPY ms_fonts /usr/local/share/fonts/ms_fonts
#RUN chmod 644 /usr/local/share/fonts/ms_fonts/* \
    #    && chmod 755 /usr/local/share/fonts/ms_fonts \
    #    && fc-cache -fv
ENV PATH="/opt/node-v8.12.0-linux-x64/bin:${PATH}"
WORKDIR /
#ENV PUPPETEER_DOWNLOAD_HOST="https://storage.googleapis.com.cnpmjs.org"
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
RUN npm i puppeteer commander inquirer --unsafe-perm=true --save
#RUN PUPPETEER_DOWNLOAD_HOST="https://storage.googleapis.com.cnpmjs.org" \
#&& npm --registry=https://registry.npm.taobao.org --disturl=https://npm.taobao.org/dist \
#    i puppeteer  --unsafe-perm=true 

WORKDIR /var/www/html

EXPOSE 80
CMD ["apache2-foreground"]
