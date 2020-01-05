FROM ruby:2.4.3-stretch

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* \
	&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8


RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main' > /etc/apt/sources.list.d/pgdg.list

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update \
	&& apt-get install -y \
		postgresql-client-9.5 \
		curl build-essential \
    imagemagick openssh-client \
    libmagickwand-dev git libsqlite3-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
## Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
## Install packages
RUN apt-get update -qq && apt-get install -y -qq  nodejs yarn
RUN gem install bundler --no-ri --no-rdoc
