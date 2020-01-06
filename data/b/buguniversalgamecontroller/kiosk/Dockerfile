FROM composer

RUN apk add --no-cache libpng libjpeg-turbo freetype libpng-dev libjpeg-turbo-dev freetype-dev
RUN   docker-php-ext-configure gd \
    --with-jpeg-dir=/usr/include/ \
    --with-freetype-dir=/usr/include/ \
    --with-png-dir=/usr/include/
RUN docker-php-ext-install gd pdo_mysql
RUN apk del libpng-dev libjpeg-turbo-dev 

RUN apk add --update nodejs npm

WORKDIR /app
COPY . .
RUN composer install --optimize-autoloader --no-dev
RUN php artisan config:clear

RUN npm install

ARG MIX_VUE_APP_BROKER=wss://api.bug.devbit.be/broker

RUN npm run production

EXPOSE 8000
EXPOSE 443
CMD [ "php", "artisan",  "serve" , "--host=0.0.0.0"]
