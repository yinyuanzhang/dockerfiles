FROM ruby:2.6
RUN apt-get update \
	&& apt-get install -y curl software-properties-common \
	&& curl -sL https://deb.nodesource.com/setup_11.x | /bin/bash -
RUN apt-get install -y nodejs \
	&& npm -g config set user root \
	&& npm install npm@latest -g

RUN npm install elm elm-live -g --quiet --no-progress
RUN gem install --no-document bundler rake middleman
RUN npm cache clean --force
CMD ["/bin/sh"]
