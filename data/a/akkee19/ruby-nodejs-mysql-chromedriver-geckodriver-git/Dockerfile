FROM ruby:latest
MAINTAINER akkee19 <akashsrvstv@yahoo.in>

RUN apt-get update
RUN apt-get --yes install gnupg
#RUN set -ex; \
# gpg: key 5072E1F5: public key "MySQL Release Engineering <mysql-build@oss.oracle.com>" imported
 # key='A4A9406876FCBD3C456770C88C718D3B5072E1F5'; \
  #export GNUPGHOME="$(mktemp -d)"; \
  #gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \
 # gpg --export "$key" > /etc/apt/trusted.gpg.d/mysql.gpg; \
#  rm -rf "$GNUPGHOME"; \
#  apt-key list > /dev/null

ENV MYSQL_MAJOR 5.7
ENV MYSQL_VERSION 5.7.22-1debian9

RUN echo "deb http://repo.mysql.com/apt/debian/ stretch mysql-${MYSQL_MAJOR}" > /etc/apt/sources.list.d/mysql.list

# # install mysql client, redis client, nodejs, chromedriver
RUN apt-get update
RUN apt-get install --yes software-properties-common build-essential libssl-dev
RUN apt-get install --yes --allow-unauthenticated  mysql-community-client libmysqlclient-dev
RUN apt-get install --yes curl wget xvfb unzip imagemagick libmagickwand-dev
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install --yes nodejs
RUN apt-get install --yes libxss1 libappindicator1 libindicator7
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update
RUN apt-get install --yes google-chrome-stable
RUN wget -N http://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip && \
 unzip chromedriver_linux64.zip && \
 chmod +x chromedriver && \
 mv -f chromedriver /usr/local/share/chromedriver && \
 ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver && \
 ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
RUN apt-get install --yes git-all
ADD . /data