FROM lsiobase/xenial
MAINTAINER peavers@gmail.com

# global environment settings
ENV DEBIAN_FRONTEND="noninteractive"

# install packages
RUN \
 apt-get update && \
 apt-get install -y \
    curl \
    wget \
    unzip \
    git

# node v6
RUN \
  curl -sL https://deb.nodesource.com/setup_6.x | bash && \
  apt-get install -y nodejs

# pm2
RUN npm install pm2 -g

# rclone
RUN cd /tmp \
  && wget -q http://downloads.rclone.org/rclone-current-linux-386.zip \
  && unzip /tmp/rclone-current-linux-386.zip \
  && mv /tmp/rclone-*-linux-386/rclone /usr/bin \
  && rm -r /tmp/rclone*

## add local files
COPY root/ /

EXPOSE 3000