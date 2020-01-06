FROM ubuntu:latest

ENV RUBY_MAJOR=2.6 \
  RUBY_VERSION=2.6.5 \
  GEM_HOME=/usr/local/bundle

ENV BUNDLE_PATH=$GEM_HOME \
  BUNDLE_APP_CONFIG=$GEM_HOME \
  BUNDLE_BIN=$GEM_HOME/bin \
  PATH=$GEM_HOME/bin:$GEM_HOME/gems/bin:$PATH \
  DEBIAN_FRONTEND=noninteractive \
  APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=true

RUN set -ex \
  && mkdir -p /usr/local/etc \
  && { echo 'install: --no-document' ; echo 'update: --no-document'; } > /usr/local/etc/gemrc \
  && buildDeps=' \
    curl \
    autoconf \
    build-essential \
    ruby \
  ' \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    $buildDeps \
    libjemalloc-dev \
    zlib1g-dev \
    libssl-dev \
    libreadline-dev \
  && rm -rf /var/lib/apt/lists/* \
  && curl -sSL "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" -o ruby.tar.xz \
  && mkdir -p /usr/src/ruby && mkdir -p "$GEM_HOME" && chmod 777 "$GEM_HOME" \
  && tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \
  && rm ruby.tar.xz \
  && cd /usr/src/ruby \
  && { echo '#define ENABLE_PATH_CHECK 0'; echo; cat file.c; } > file.c.new \
  && mv file.c.new file.c \
  && autoconf \
  && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
  && ./configure \
    --build="$gnuArch" \
    --disable-install-doc \
    --enable-shared \
    --with-jemalloc \
  && make -j "$(nproc)" \
  && make install \
  && apt-get purge -y --auto-remove $buildDeps \
  && cd / \
  && rm -r /usr/src/ruby \
  && echo "LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libjemalloc.so.1" > /etc/environment

CMD irb
