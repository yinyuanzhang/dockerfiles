FROM ubuntu:latest

MAINTAINER Alex Pringle <alex@alexpringle.co.uk>

# Elixir requires UTF-8
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# update and install some software requirements
RUN apt-get update && apt-get upgrade -y && apt-get install -y curl wget git make

# download and install Erlang package
RUN wget http://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \
 && dpkg -i erlang-solutions_1.0_all.deb \
 && apt-get update

# install psql
RUN  sudo apt-get -yqq install postgresql-client

# install erlang from package
RUN apt-get install -y erlang erlang-ssl erlang-inets && rm erlang-solutions_1.0_all.deb

ENV ELIXIR_VERSION 1.2.0
# install elixir from source
RUN git clone https://github.com/elixir-lang/elixir.git && cd elixir && git checkout v$ELIXIR_VERSION && make
ENV PATH $PATH:/elixir/bin

ENV PHOENIX_VERSION 1.1.2

# install Phoenix from source with some previous requirements
RUN git clone https://github.com/phoenixframework/phoenix.git
WORKDIR /phoenix
RUN git checkout v$PHOENIX_VERSION
RUN mix local.hex --force && mix local.rebar --force \
 && mix do deps.get, compile
RUN cd installer && MIX_ENV=prod mix archive.build \
 && mix archive.install --force && cd ..

# install Node.js and NPM in order to satisfy brunch.io dependencies
# the snippet below is borrowed from the official nodejs Dockerfile
# https://registry.hub.docker.com/_/node/

# verify gpg and sha256: http://nodejs.org/dist/v$NODE_VERSIONSHASUMS256.txt.asc
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

ENV NODE_VERSION 5.5.0
ENV NPM_VERSION 3.3.12

RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-linux-x64.tar.gz" \
 && curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \
 && gpg --verify SHASUMS256.txt.asc \
 && grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc | sha256sum -c - \
 && tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local --strip-components=1 \
 && rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \
 && npm install -g npm@"$NPM_VERSION" \
 && npm cache clear

WORKDIR /code

ONBUILD COPY package.json /code
ONBUILD COPY . /code
ONBUILD RUN mix deps.get
ONBUILD RUN npm install
