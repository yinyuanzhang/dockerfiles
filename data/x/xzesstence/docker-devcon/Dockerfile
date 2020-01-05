FROM xzesstence/docker-ubuntu:latest
MAINTAINER "Tim Koepsel"

RUN apt-get update
RUN apt-get install -q -y nodejs && apt-get install -q -y npm
RUN apt-get install -q -y openssh-server

RUN npm install -g grunt && npm install -g gulp && npm install -g rubygems
RUN curl https://install.meteor.com/ | sh

RUN useradd -d /home/xdev -ms /bin/bash -g root -G sudo xdev
RUN echo 'xdev:123456' | chpasswd
USER xdev
WORKDIR /home/xdev

RUN echo 'alias xrefresh="source ~/.bash_aliases"' >> ~/.bash_aliases
RUN echo 'alias xwww="cd /var/www/html"' >> ~/.bash_aliases
RUN echo 'alias xalias="sudo vi ~/.bash_aliases"' >> ~/.bash_aliases
RUN echo 'alias xspace="df -h"' >> ~/.bash_aliases
RUN /bin/bash -c "source ~/.bash_aliases"


CMD sudo /etc/init.d/ssh start
RUN bash
