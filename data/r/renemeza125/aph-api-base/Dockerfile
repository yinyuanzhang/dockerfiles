FROM ubuntu:xenial
MAINTAINER Rene Meza <rene.meza125@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Ruby env variables
ENV RUBY_MAJOR 2.3
ENV RUBY_VERSION 2.3.3
ENV RUBY_DOWNLOAD_SHA256 1a4fa8c2885734ba37b97ffdb4a19b8fba0e8982606db02d936e65bac07419dc
ENV RUBYGEMS_VERSION 2.6.10

# Set mirrors to NZ
RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git-core curl gnupg build-essential automake libtool bison wget \
    libgdbm-dev zlib1g-dev libssl-dev libreadline-dev libyaml-dev \
    libsqlite3-dev libxml2-dev libxslt1-dev libcurl4-openssl-dev libffi-dev \
    libgdbm-dev libncurses5-dev libffi-dev

# Install ruby
RUN wget -O ruby.tar.xz "http://ftp.ruby-lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" && \
    echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.xz" | sha256sum -c - && \
    mkdir -p /usr/src/ruby && \
    tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 && \
    rm ruby.tar.xz && \
    cd /usr/src/ruby && \
    { \
        echo '#define ENABLE_PATH_CHECK 0'; \
        echo; \
        cat file.c; \
    } > file.c.new && \
    mv file.c.new file.c && \
    autoconf && \
    ./configure --disable-install-doc --enable-shared && \
    make && \
    make install && \
    apt-get purge -y --auto-remove bison libgdbm-dev ruby && \
    cd / && \
    rm -r /usr/src/ruby && \
    gem update --system "$RUBYGEMS_VERSION"

ENV BUNDLER_VERSION 1.14.4

# Install bundler
RUN gem install bundler --no-ri --no-rdoc --version "$BUNDLER_VERSION"

# Install gems globally
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
    BUNDLE_BIN="$GEM_HOME/bin" \
    BUNDLE_SILENCE_ROOT_WARNING=1 \
    BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH

RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" \
    && chmod 777 "$GEM_HOME" "$BUNDLE_BIN"

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

LABEL application=aph-api