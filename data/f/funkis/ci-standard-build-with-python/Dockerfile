FROM node:10.9.0

RUN cd ~ && npm install npm@6.0.0 && rm -rf /usr/local/lib/node_modules && mv node_modules /usr/local/lib/

RUN apt-get update && apt-get upgrade -y \
  && apt-get install rsync python-dev -y \
  && npm install -g grunt-cli
