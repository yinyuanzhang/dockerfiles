FROM        debian:latest

# Common tools
RUN         apt-get update && apt-get install -y curl git acl mc ruby ruby-dev

# PHP5 & mySQL client
RUN         apt-get update && apt-get install -y php5-cli php5-curl php5-gd php5-mcrypt php5-mysql mysql-client

# Node JS
RUN         curl -sL https://deb.nodesource.com/setup | bash -
RUN         apt-get update && apt-get install -y nodejs

# Bower
RUN         npm install -g bower

# Sass
RUN         gem install sass

# Compass
#RUN         gem install compass

# Composer
WORKDiR     /usr/bin/
RUN         curl -sS https://getcomposer.org/installer | php
RUN         mv composer.phar composer

# WkHtmlToPdf
RUN         apt-get update && apt-get install -y wkhtmltopdf xvfb

WORKDIR     /