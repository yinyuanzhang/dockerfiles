FROM php:5.6-apache

RUN apt-get -qq update \
        && apt-get install --assume-yes --no-install-recommends apt-utils zip curl mysql-client git ruby-dev rubygems \
        && gem update --system \
        && gem install compass \
        && gem install dpl \
        && gem install aws-sdk

CMD ["apache2-foreground"]
