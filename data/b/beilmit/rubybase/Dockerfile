FROM buildpack-deps:stretch
MAINTAINER Takashi Kurosawa

ENV DEBIAN_FRONTEND noninteractive
ENV RUBY_MAJOR 2.4
ENV RUBY_VERSION 2.4.4
ENV RUBY_DOWNLOAD_SHA256 1d0034071d675193ca769f64c91827e5f54cb3a7962316a41d5217c7bc6949f0
ENV RUBYGEMS_VERSION 2.7.6
ENV BUNDLER_VERSION 1.16.1
ENV DOCKERIZE_VERSION v0.3.0
ENV ENTRYKIT_VERSION 0.4.0
ENV JQ_VERSION 1.5
ENV DOCKER 1
ENV DEBIAN_FRONTEND noninteractive
ENV TZ Asia/Tokyo
ENV HOME /root
ENV PATH /app/vendor/bundle/bin:/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin

RUN mkdir -p /usr/local/etc
RUN set -ex \
    && buildDeps=' \
     bison \
     dpkg-dev \
     libgdbm-dev \
     ruby \
    ' \
    && apt-get update \
    && apt-get install -y --no-install-recommends $buildDeps \
    && rm -rf /var/lib/apt/lists/* \
    && wget -O ruby.tar.xz "https://cache.ruby-lang.org/pub/ruby/${RUBY_MAJOR}/ruby-$RUBY_VERSION.tar.xz" \
    && echo "$RUBY_DOWNLOAD_SHA256 *ruby.tar.xz" | sha256sum -c - \
    && mkdir -p /usr/src/ruby \
    && tar -xJf ruby.tar.xz -C /usr/src/ruby --strip-components=1 \
    && rm ruby.tar.xz \
    && cd /usr/src/ruby \
    && { \
     echo '#define ENABLE_PATH_CHECK 0'; \
     echo; \
     cat file.c; \
    } > file.c.new \
    && mv file.c.new file.c \
    && autoconf \
    && gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
    && ./configure \
     --build="$gnuArch" \
     --disable-install-doc \
     --enable-shared \
    && make -j "$(nproc)" \
    && make install \
    && apt-get purge -y --auto-remove $buildDeps \
    && cd / \
    && rm -fr /usr/src/ruby \
    && gem update --system "$RUBYGEMS_VERSION" \
    && gem install bundler --version "$BUNDLER_VERSION" --force

RUN apt-get update -qq \
    && apt-get install -y build-essential mysql-client \
     default-libmysqlclient-dev sudo curl wget zip unzip git wget \
     ca-certificates openssl telnet sqlite3 \
     dnsutils libxml2-dev libreadline-dev vim less postfix cron rsyslog \
    && echo "${TZ}" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata \
    && rm -f /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && wget https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
    && tar -xvzf entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
    && rm entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
    && mv entrykit /bin/entrykit \
    && chmod +x /bin/entrykit \
    && entrykit --symlink

# nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash \
    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
    && echo "deb https://dl.yarnpkg.com/debian/ stable main" > /etc/apt/sources.list.d/yarn.list \
    && apt-get update && apt-get -y install nodejs yarn

# Chrome & Japanese font Noto
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - \
    && sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && wget https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip \
    && unzip NotoSansCJKjp-hinted.zip NotoSansCJKjp-Regular.otf NotoSansCJKjp-Bold.otf -d /usr/share/fonts/noto/ \
    && fc-cache -fv

# ChromeDriver
RUN CHROMEDRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE` \
    && mkdir -p /opt/chromedriver-$CHROMEDRIVER_VERSION \
    && curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
    && unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-$CHROMEDRIVER_VERSION \
    && rm /tmp/chromedriver_linux64.zip \
    && chmod +x /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver \
    && ln -fs /opt/chromedriver-$CHROMEDRIVER_VERSION/chromedriver /usr/local/bin/chromedriver

# jq
RUN wget -q -O /usr/local/bin/jq https://github.com/stedolan/jq/releases/download/jq-$JQ_VERSION/jq-linux64 \
    && chmod 755 /usr/local/bin/jq

# vim
RUN printf 'set softtabstop=2\nset tabstop=2\nautocmd FileType * setlocal formatoptions-=ro\n' > /root/.vimrc
RUN echo 'gem: --no-rdoc --no-ri' > /root/.gemrc
RUN bundle config disable_shared_gems 1
RUN bundle config path vendor/bundle
RUN bundle config build.nokogiri --use-system-libraries

WORKDIR /app
