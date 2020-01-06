# Version 1.0
FROM google/nodejs
MAINTAINER Jack Liu <chuany@ms6.hinet.net>

WORKDIR /home
RUN	git clone https://github.com/shrikrishnaholla/code.it.git

WORKDIR code.it
RUN	git submodule update --init --recursive
RUN	npm install

EXPOSE	8000

WORKDIR /home
CMD	["/usr/bin/node", "/home/code.it/app.js"]

