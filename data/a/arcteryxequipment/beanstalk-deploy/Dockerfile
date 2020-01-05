# Ubuntu Xenial = 16.04
FROM ubuntu:xenial

LABEL vendor="Arc'teryx Equipment"
LABEL maintainer="Web Team"
LABEL com.arcteryx.version="0.1.0"
LABEL com.arcteryx.release-date="2018-12-14"

RUN apt-get update && apt-get install -y \
  curl \ 
  wget \
  zip \
  git \
  python-pip \ 
  nginx \
  gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

# Node 8
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs

# AWS CLI
RUN pip install awscli --upgrade

# AWS `eb` CLI
RUN pip install awsebcli --upgrade

# PHP 7.2
RUN apt-get install -y software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN apt-get install -y php7.2 php7.2-cli php7.2-common
RUN apt-get install -y php7.2-mbstring php7.2-xml php7.2-gd php7.2-curl

COPY composer-install.sh /root/

RUN /root/composer-install.sh
