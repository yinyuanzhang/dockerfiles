FROM pykiss/node
LABEL version="1.1"

ENV NPM_SCRIPT bash
ENV NODE_ENV development

RUN apt-get install -yqq ruby-full sudo
RUN gem install sass
RUN gem install compass
RUN ln /usr/bin/nodejs /usr/bin/node
RUN npm install -g bower
RUN npm install -g grunt-cli

