FROM xzesstence/docker-ubuntu:latest
MAINTAINER "Tim Koepsel"

# Install Basics
RUN apt-get update && apt-get install -q -y curl
RUN apt-get install -q -y openssh-server

# Configure Timezone
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Webserver
RUN apt-get install -q -y nginx

# Install MySQL
ENV MYSQL_PWD 123456
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PWD" | debconf-set-selections
RUN echo "mysql-server mysql-server/root_password_again password $MYSQL_PWD" | debconf-set-selections
RUN apt-get -y -q install mysql-server mysql-client

# Install PHP7 and Libs
RUN apt-get -y install php7.0
RUN apt-get -y install php-all-dev
# Install NPM and Node and RubyGems
RUN apt-get install -q -y nodejs && apt-get install -q -y npm
RUN npm install -g grunt && npm install -g gulp && npm install -g rubygems

# Install Meteor
RUN curl https://install.meteor.com/ | sh


# Add Default User
RUN useradd -d /home/xdev -ms /bin/bash -g root -G sudo xdev
RUN echo 'xdev:123456' | chpasswd
USER xdev
WORKDIR /home/xdev


# Add some aliases
RUN echo 'alias xrefresh="source ~/.bash_aliases"' >> ~/.bash_aliases
RUN echo 'alias xwww="cd /var/www/html"' >> ~/.bash_aliases
RUN echo 'alias xalias="sudo vi ~/.bash_aliases"' >> ~/.bash_aliases
RUN echo 'alias xspace="df -h"' >> ~/.bash_aliases
RUN /bin/bash -c "source ~/.bash_aliases"

# Start services
CMD sudo service ssh start && bash
CMD sudo service nginx start