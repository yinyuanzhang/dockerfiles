FROM phommel/golang

MAINTAINER phommel

RUN apt-get update -qq && apt-get upgrade -y && apt-get install -y \
    g++ \
    flex \
    bison \
    gperf \
    ruby \
    perl \
    libsqlite3-dev \
    libfontconfig1-dev \
    libicu-dev \
    libfreetype6 \
    libssl-dev \
    libpng-dev \
    libjpeg-dev \
    libqt5webkit5-dev

ENV PHANTOM_JS_TAG 2.0.0

RUN git clone https://github.com/ariya/phantomjs.git /tmp/phantomjs
RUN cd /tmp/phantomjs && git checkout $PHANTOM_JS_TAG && \
  ./build.sh --confirm && mv bin/phantomjs /usr/local/bin

RUN apt-get clean
RUN rm -rf /tmp/* /var/tmp/*