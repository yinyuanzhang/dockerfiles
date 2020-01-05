FROM ruby:2.3.3

RUN \
  curl -sL https://deb.nodesource.com/setup_6.x | bash - && \
  apt-get update && \
  apt-get install -y --no-install-recommends mysql-client nodejs && \
  curl -LOs https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
  tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
  cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/ && \
  rm -r phantomjs-2.1.1-linux-x86_64 phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
  curl -LOs http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz && \
  gunzip GeoLiteCity.dat.gz && \
  mkdir -p /usr/share/GeoIP/ && \
  mv GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/*
