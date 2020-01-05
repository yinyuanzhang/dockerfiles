FROM ruby:2.6.5-stretch

ENV LANG C.UTF-8
ENV IMAGE_MAGICK_VERSION 7.0.8-27

RUN echo "deb http://ftp.uk.debian.org/debian stretch-backports main" >> /etc/apt/sources.list \
    && apt-get update -qq \
    && apt-get install -y --no-install-recommends \
    build-essential \
    unzip \
    gdebi \
    libpq-dev \
    libfontconfig1 \
    libreadline-dev \
    libmagickwand-dev \
    libcurl3 libcurl3-gnutls \
    libcurl4-openssl-dev \
    libssl-dev \
    gettext \
    libpcre3 \
    libpcre3-dev \
    libxml2-dev \
    libxslt-dev \
    libgd-dev \
    libgeoip-dev \
    libmariadbclient-dev \
    ffmpeg \
    fonts-ipafont-gothic \
    libnss3 \
    libmecab-dev \
    mecab \
    mecab-ipadic-utf8 \
    && git clone https://github.com/kornelski/giflossy.git \
    && cd giflossy \
    && autoreconf -i \
    && ./configure \
    && make \
    && make install \
    && cd ../ \
    && rm -fr giflossy \
    && git clone https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && ./bin/install-mecab-ipadic-neologd -n -y \
    && cd ../ && rm -fr mecab-ipadic-neologd \
    && mv /etc/mecabrc /etc/mecabrc.old \
    && sed -e s@/var/lib/mecab/dic/debian@/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd@g /etc/mecabrc.old > /etc/mecabrc \
    && cd ../ \
    && rm -fr mecab-ipadic-neologd \
    && wget -q https://chromedriver.storage.googleapis.com/2.42/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin/chromedriver \
    && chmod 755 /usr/bin/chromedriver \
    && rm chromedriver_linux64.zip \
    && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && gdebi -n google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb \
    && curl -sL https://deb.nodesource.com/setup_8.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/* \
    && npm i -g npm \
    && npm install -g phantomjs-prebuilt --unsafe-perm \
    && echo "Cleaning up image. see https://github.com/janeczku/docker-debian-s6/blob/master/docker/wheezy-backports/rootfs/usr/bin/apt-clean" \
    && apt-get autoremove -y \
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb /var/cache/apt/*.bin

ENV ENTRYKIT_VERSION 0.4.0
RUN wget -q https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
    && tar -xvzf entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
    && rm entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \
    && mv entrykit /bin/entrykit \
    && chmod +x /bin/entrykit \
    && entrykit --symlink

RUN mkdir /app

WORKDIR /app

RUN bundle config build.nokogiri --use-system-libraries

ENTRYPOINT [ \
  "prehook", "ruby -v", "--", \
  "prehook", "bundle install -j3 --quiet", "--"]
