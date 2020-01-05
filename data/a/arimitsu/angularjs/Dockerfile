FROM node:6.9
MAINTAINER Y.Arimitsu<arimitu@ouk.jp>

# Grunt & Bower のインストール
RUN npm install -g grunt bower

# Ruby&compass
RUN apt-get update && apt-get install -y ruby ruby-dev

## http://stackoverflow.com/questions/39269285/compass-provision-failing-with-docker-compose-up
RUN gem update
RUN gem install --no-rdoc --no-ri sass -v 3.4.22
RUN gem install --no-rdoc --no-ri compass

EXPOSE 9000 35729

WORKDIR /home
VOLUME /home