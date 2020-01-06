FROM devwithlando/php:7.1-apache

RUN apt-get update \
    && apt-get install -my wget gnupg \
    && curl -sL https://deb.nodesource.com/setup_9.x | bash - \
    && apt-get install -y nodejs \
    && apt-get install -y git
