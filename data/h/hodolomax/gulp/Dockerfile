FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl git
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash /dev/stdin
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential
RUN npm install -g node-gyp
RUN npm install -g gulp@3.9.1
RUN npm install -g bower
RUN npm install sass bower-npm-resolver
