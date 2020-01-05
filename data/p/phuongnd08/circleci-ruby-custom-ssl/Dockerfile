FROM buildpack-deps:jessie
LABEL description="Circle Ci Ruby 2.4.3 with custom open ssl"
LABEL version="2.4.3"

RUN mkdir -p /build/openssl
WORKDIR /build/openssl
ENV OPENSSL_VERSION 1.0.1f
RUN curl -s https://www.openssl.org/source/openssl-${OPENSSL_VERSION}.tar.gz | tar -C /build/openssl -xzf - && \
    cd /build/openssl/openssl-${OPENSSL_VERSION} && \
    ./Configure \
      --openssldir=/opt/openssl/openssl \
      shared linux-x86_64 && \
    make && make install_sw

# https://github.com/docker-library/ruby/blob/master/2.3/jessie/Dockerfile
# skip installing gem documentation
RUN mkdir -p /usr/local/etc \
	&& { \
		echo 'install: --no-document'; \
		echo 'update: --no-document'; \
	} >> /usr/local/etc/gemrc

ENV RUBY_MAJOR 2.4
ENV RUBY_VERSION 2.4.3
ENV RUBY_DOWNLOAD_SHA256 23677d40bf3b7621ba64593c978df40b1e026d8653c74a0599f0ead78ed92b51
ENV RUBYGEMS_VERSION 2.7.6
ENV BUNDLER_VERSION 1.16.1

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
    --with-openssl-dir="/opt/openssl/openssl" \
	&& make -j "$(nproc)" \
	&& make install \
	\
	&& apt-get purge -y --auto-remove $buildDeps \
	&& cd / \
	&& rm -r /usr/src/ruby \
	\
	&& gem update --system "$RUBYGEMS_VERSION" \
	&& gem install bundler --version "$BUNDLER_VERSION" --force \
	&& rm -r /root/.gem/

RUN mkdir -p /build/bx
WORKDIR /build/bx
RUN curl -L -O https://github.com/libbitcoin/libbitcoin-explorer/releases/download/v3.2.0/bx-linux-x64-qrcode
RUN chmod u+x bx-linux-x64-qrcode
RUN mv bx-linux-x64-qrcode /usr/local/bin/bx

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

RUN apt-get update && apt-get install -y build-essential nodejs
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get install -y nodejs
RUN apt-get install -y libzmq3-dev
RUN npm install -g yarn

ENV LC_ALL "C.UTF-8"
ENV LANG "en_uC.UTF-8"
ENV LANGUAGE="en_US.UTF-8"
