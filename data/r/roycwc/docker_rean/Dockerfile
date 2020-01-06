FROM ubuntu
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get update
RUN apt-get install -y curl wget openssh-server

# Install sshd
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

# Install rethinkdb
RUN source /etc/lsb-release && echo "deb http://download.rethinkdb.com/apt $DISTRIB_CODENAME main" | sudo tee /etc/apt/sources.list.d/rethinkdb.list
RUN wget -qO- https://download.rethinkdb.com/apt/pubkey.gpg | sudo apt-key add -
RUN apt-get update
RUN apt-get install -y rethinkdb

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash -
RUN apt-get install -y nodejs

# Install forever
RUN npm install -g forever

# Install express app in /var/www/node
RUN mkdir /var/www
RUN mkdir /var/www/node
RUN cd /var/www/node
RUN npm install express
RUN echo "var express = require('express');var app = express();app.get('/', function(req, res){res.send('Hello World');});app.listen(80);" > /var/www/node/app.js

# Start app, watch file changes, output log
RUN echo $'#!/bin/bash \n\
/usr/sbin/sshd -D & \n\
rethinkdb --bind all & \n\
sleep 3 && cd /var/www/node && forever -w -l rean.log start app.js & \n\
tail -n 50 -F /root/.forever/rean.log' > /etc/startup.sh
RUN chmod 755 /etc/startup.sh

EXPOSE 22 8080 80
CMD ["/etc/startup.sh"]