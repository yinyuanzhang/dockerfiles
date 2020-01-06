FROM ruby:jessie
MAINTAINER thibault.theologien@insa-rouen.fr
WORKDIR /root

RUN apt-get update
RUN apt-get install nodejs npm -y
RUN npm install -g n
RUN npm install npm@latest -g
RUN n stable
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN gem install sass
RUN gem install sass-json-vars
RUN npm install --global gulp-cli
RUN apt-get install locales locales-all -y

ENV LC_ALL=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US.UTF-8
RUN rm -rf /var/lib/apt/lists/*

CMD npm install
