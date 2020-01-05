FROM ruby:2.5
MAINTAINER	Mekapiku <mekapiku@gmail.com>

# Environment
ENV OUTPUT_DIR="/tmp/kanden.json"
ENV KANDEN_LOGIN_ID="USER_ID"
ENV KANDEN_LOGIN_PASS="USER_PASS"

# http://phantomjs.org/build.html
# https://github.com/sparklemotion/nokogiri.org-tutorials/blob/master/content/installing_nokogiri.md
RUN apt-get update \
  && apt-get install -y git curl build-essential g++ flex bison gperf ruby perl \
  libsqlite3-dev libfontconfig1-dev libicu-dev libfreetype6 libssl-dev \
  libpng-dev libjpeg-dev python libx11-dev libxext-dev \
  && apt-get clean

# Install Phantomjs
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN tar jxfv phantomjs-2.1.1-linux-x86_64.tar.bz2
RUN mv phantomjs-2.1.1-linux-x86_64 /usr/local/src/phantomjs
RUN cd /usr/local/src
RUN ln -s /usr/local/src/phantomjs/bin/phantomjs /usr/local/bin/phantomjs

# Cache poltergeist gem
RUN gem install nokogiri
RUN gem install poltergeist
RUN gem install capybara

# Add Ruby Script
RUN cd /root && export GIT_SSL_NO_VERIFY=1 && \
    git config --global http.sslVerify false && \
    git clone https://github.com/Mekapiku/KandenAPI.git

# Exec app
WORKDIR /root/KandenAPI
CMD cd /root/KandenAPI && ruby ./app.rb ${OUTPUT_DIR} ${KANDEN_LOGIN_ID} ${KANDEN_LOGIN_PASS}
