# Set the base image to Ubuntu
FROM    ubuntu:14.04

# File Author / Maintainer
MAINTAINER Gustavo Stor

# Install Node.js and other dependencies
RUN apt-get update && \
    apt-get -y install curl && \
    curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \
    apt-get -y install nodejs git-all build-essential vim supervisor nginx

# Install node_modules and bower_components
RUN npm install -g grunt-cli bower node-gyp
COPY package.json /tmp/
RUN cd /tmp && npm install
COPY [".bowerrc", "bower.json", "/tmp/"]
RUN cd /tmp && bower install --allow-root

# Set up working directory
RUN mkdir -p /www
WORKDIR /www
ADD . /www

RUN cp -a /tmp/node_modules /www/ && \
    cp -a /tmp/public/bower_components /www/public/ && \
    rm -rf /tmp && \
    grunt prod && \
    mkdir -p /var/log/supervisor && \
    rm -rf /etc/nginx/conf.d/* && \
    rm -rf /etc/nginx/sites-enabled/*

# Set up config files
COPY .prod/default.conf /etc/nginx/conf.d/
COPY .prod/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]
