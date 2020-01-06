FROM pataquets/ubuntu:trusty

ENV PHANTOM_JS_TAG 2.0.0

RUN \
  echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu $(lsb_release -cs) main" \
    | tee /etc/apt/sources.list.d/git.list && \
  DEBIAN_FRONTEND=noniteractive \
    apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys E1DF1F24 && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y --no-install-recommends install git && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      libfontconfig1 \
      libjpeg8 \
      libicu52 \
  && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y install \
      build-essential \
      g++ flex bison gperf ruby perl python \
      libsqlite3-dev libfontconfig1-dev libicu-dev \
      libfreetype6 libssl-dev libpng-dev libjpeg-dev \
# Note: It is recommend also to install ttf-mscorefonts-installer package.
# (http://phantomjs.org/build.html)
#      ttf-mscorefonts-installer \
  && \
  git clone https://github.com/ariya/phantomjs.git /tmp/phantomjs && \
  cd /tmp/phantomjs && \
  git checkout ${PHANTOM_JS_TAG} && \
  ./build.sh --confirm && \
  mv bin/phantomjs /usr/local/bin && \
  rm -rf /tmp/phantomjs \
  && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get -y purge \
      build-essential \
      g++ flex bison gperf ruby perl python \
      libsqlite3-dev libfontconfig1-dev libicu-dev \
      libssl-dev libpng-dev libjpeg-dev \
  && \
  DEBIAN_FRONTEND=noninteractive \
    apt-get autoremove --purge -y && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*
