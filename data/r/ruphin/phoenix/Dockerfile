FROM buildpack-deps:jessie
MAINTAINER Goffert van Gool "goffert@phusion.nl"

# Install Erlang, Elixir
# inotify-tools, and en_US-UTF-8
################################
ENV ERLANG_VERSION 1:18.2
ENV ELIXIR_VERSION 1.2.0-1

RUN echo "deb http://packages.erlang-solutions.com/debian jessie contrib" >> /etc/apt/sources.list \
	&& wget http://packages.erlang-solutions.com/debian/erlang_solutions.asc \
	&& apt-key add erlang_solutions.asc \
	&& rm erlang_solutions.asc \
	&& apt-get update && apt-get install -y locales inotify-tools esl-erlang=$ERLANG_VERSION elixir=$ELIXIR_VERSION && apt-get clean && apt-get purge \
	&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
	&& locale-gen \

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# Install Node
##############
ENV NODE_VERSION 5.5.0

RUN set -ex \
	&& for key in \
	  9554F04D7259F04124DE6B476D5A82AC7E37093B \
	  94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \
	  0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \
	  FD3A5288F042B6850C66B31F09FE44734EB7990E \
	  71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \
	  DD8F2338BAE7501E3DD5AC78C273792F7D83545D \
	  B9AE9905FFD7803F25714661B63B535A4C206CA9 \
	  C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \
	; do \
	  gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
	done

ENV NPM_CONFIG_LOGLEVEL info

RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
	&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
	&& gpg --verify SHASUMS256.txt.asc \
	&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
	&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
	&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc

# Install Phoenix
#################
ENV HEX_VERSION 10.4

RUN echo "$HEX_VERSION" && mix local.hex --force \
	&& mix archive.install https://github.com/phoenixframework/archives/raw/master/phoenix_new.ez --force

CMD mix hex.info && mix phoenix.server
