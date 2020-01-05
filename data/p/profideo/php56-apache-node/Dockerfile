FROM profideo/php-5.6.20-fpm

MAINTAINER Alban Duval <aduval@profideo.com>

RUN apt-get install -y apt-transport-https
RUN curl -s https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add -
RUN apt-get update
RUN apt-get install nodejs npm nodejs-legacy -qq -u -y
RUN mkdir -p /home/profideo/.npm
RUN chown -R profideo:profideo /home/profideo/.npm
RUN npm install -g less
RUN npm install -g bower
RUN npm cache clean
RUN npm update -g
