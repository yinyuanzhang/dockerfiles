FROM phpmentors/symfony-app:php72 as symfony
LABEL maintainer="Randy Tellez Galán <kronhyx@gmail.com>"
RUN apt-get install -yyq git wget zip unzip curl
RUN curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer
