FROM abiskop/base

RUN echo deb http://archive.ubuntu.com/ubuntu precise main universe > /etc/apt/sources.list
RUN echo deb http://archive.ubuntu.com/ubuntu precise-updates main universe >> /etc/apt/sources.list

RUN echo deb http://ppa.launchpad.net/nginx/stable/ubuntu precise main > /etc/apt/sources.list.d/nginx-stable-precise.list
RUN echo deb-src http://ppa.launchpad.net/nginx/stable/ubuntu precise main >> /etc/apt/sources.list.d/nginx-stable-precise.list

RUN apt-get update
RUN apt-get upgrade -y --no-install-recommends

RUN apt-get install -y --force-yes nginx
RUN nginx -v

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

