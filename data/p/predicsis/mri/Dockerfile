FROM ubuntu:trusty
MAINTAINER mdouchement

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get upgrade -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy bash curl git \
      build-essential \
      zlib1g-dev \
      libssl-dev \
      libreadline6-dev \
      libyaml-dev \
      procps \
      nodejs \
      vim

RUN cd /usr/bin; ln -s /usr/bin/nodejs node

ENV RUBY_MAJOR 2.1
ENV RUBY_VERSION 2.1.2

# some of ruby's build scripts are written in ruby
# we purge this later to make sure our final image uses what we just built
RUN apt-get install -y bison ruby autoconf \
    && mkdir -p /usr/src/ruby \
    && curl -SL "http://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR}/ruby-${RUBY_VERSION}.tar.bz2" \
        | tar -xjC /usr/src/ruby --strip-components=1 \
    && cd /usr/src/ruby \
    && autoconf \
    && ./configure --disable-install-doc \
    && make -j"$(nproc)" \
    && apt-get purge -y --auto-remove bison ruby autoconf \
    && make install \
    && rm -r /usr/src/ruby

# skip installing gem documentation
RUN echo 'gem: --no-rdoc --no-ri' >> "${HOME}/.gemrc"

# install things globally, for great justice
ENV GEM_HOME /usr/local/bundle
ENV PATH $GEM_HOME/bin:$PATH
RUN gem install bundler \
      && bundle config --global path "${GEM_HOME}" \
      && bundle config --global bin "${GEM_HOME}/bin"

CMD irb
