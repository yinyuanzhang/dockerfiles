FROM node:8.11.1-stretch
# DO NOT CHANGE THIS WITHOUT CHANGING HOLVIKAARI NODE ENV

RUN apt-get update -y && apt-get install -y --no-install-recommends \
	git \
	qt5-default \
	libqt5webkit5-dev \
	xvfb \
	xauth \
	default-jre \
	curl unzip \
	xvfb tinywm \
	fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic \
	python \
	python-pip \
	python-dev \
	python-setuptools \
	&& rm -rf /var/lib/apt/lists

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# skip installing gem documentation
RUN mkdir -p /usr/local/etc \
	&& { \
	echo 'install: --no-document'; \
	echo 'update: --no-document'; \
	} >> /usr/local/etc/gemrc

ENV RUBY_MAJOR 2.4
ENV RUBY_VERSION 2.4.6
ENV RUBYGEMS_VERSION 3.0.3

# some of ruby's build scripts are written in ruby
#   we purge system ruby later to make sure our final image uses what we just built
RUN set -ex \
	\
	&& buildDeps=' \
	bison \
	libgdbm-dev \
	ruby \
	' \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends $buildDeps netcat postgresql-client \
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& wget -O ruby.tar.xz "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR%-rc}/ruby-$RUBY_VERSION.tar.xz" \
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
	&& ./configure --disable-install-doc --enable-shared \
	&& make -j"$(nproc)" \
	&& make install \
	\
	&& apt-get purge -y --auto-remove $buildDeps \
	&& cd / \
	&& rm -r /usr/src/ruby \
	\
	&& gem update --system "$RUBYGEMS_VERSION"

# install things globally, for great justice
# and don't create ".bundle" in all our apps
ENV GEM_HOME /usr/local/bundle
ENV BUNDLE_PATH="$GEM_HOME" \
	BUNDLE_BIN="$GEM_HOME/bin" \
	BUNDLE_SILENCE_ROOT_WARNING=1 \
	BUNDLE_APP_CONFIG="$GEM_HOME"
ENV PATH $BUNDLE_BIN:$PATH
RUN mkdir -p "$GEM_HOME" "$BUNDLE_BIN" && chmod 777 "$GEM_HOME" "$BUNDLE_BIN"

ENV BUNDLER_VERSION 2.0.1
RUN gem install bundler --version "$BUNDLER_VERSION"

# Setup Code Climate test-reporter (https://docs.codeclimate.com/docs/configuring-test-coverage)
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > /usr/bin/cc-test-reporter && chmod +x /usr/bin/cc-test-reporter

RUN pip install awscli

# Install Google Chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
	echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
	apt-get -yqq update && \
	apt-get -yqq install google-chrome-stable && \
	rm -rf /var/lib/apt/lists/*

# Install Chrome WebDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_75` && \
  wget -N http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip -P ~/ && \
  unzip ~/chromedriver_linux64.zip -d ~/ && \
  rm ~/chromedriver_linux64.zip && \
  mv -f ~/chromedriver /usr/local/bin/chromedriver && \
  chown root:root /usr/local/bin/chromedriver && \
  chmod 0755 /usr/local/bin/chromedriver

RUN CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)" && \
  curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
  echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
  apt-get -yqq update && apt-get -yqq install google-cloud-sdk

# Default configuration
ENV DISPLAY :20.0
ENV SCREEN_GEOMETRY "1440x900x24"
ENV CHROMEDRIVER_PORT 4444
ENV CHROMEDRIVER_WHITELISTED_IPS "127.0.0.1"
ENV CHROMEDRIVER_URL_BASE ''
ENV CHROMEDRIVER_EXTRA_ARGS ''

EXPOSE 4444

CMD [ "irb" ]
