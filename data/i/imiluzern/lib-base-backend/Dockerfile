FROM imiluzern/base-backend:latest

RUN cd /var/tmp && composer create-project --prefer-dist laravel/laravel composer-cache

RUN cd /var/tmp/composer-cache && php artisan app:name AG

COPY ./composer.json /var/tmp/composer-cache/composer.json

RUN cd /var/tmp/composer-cache && composer update

COPY ./package.json /var/tmp/composer-cache/package.json

COPY ./bower.json /var/tmp/composer-cache/bower.json

RUN cd /var/tmp/composer-cache && npm install && bower install --allow-root