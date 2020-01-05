
FROM mirkokiefer/node

RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe > /etc/apt/sources.list
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >> /etc/apt/sources.list
RUN apt-get update

RUN apt-get install -y imagemagick

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

