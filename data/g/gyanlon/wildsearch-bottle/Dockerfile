# A super-simple "search" server that exposes port 8080
#
# VERSION               0.1.0
FROM ubuntu:14.04
MAINTAINER Yan Long Gao <gyanlon@hotmail.com>

# Set Timezone
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Ensure UTF-8 locale
#COPY locale /etc/default/locale
RUN locale-gen zh_CN.UTF-8 && DEBIAN_FRONTEND=noninteractive dpkg-reconfigure locales
RUN locale-gen zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
ENV LANGUAGE zh_CN:zh  
ENV LC_ALL zh_CN.UTF-8

# create user
RUN groupadd web
RUN useradd -d /home/bottle -m bottle

# make sure sources are up to date
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

# Install dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common
#RUN add-apt-repository universe
RUN apt-get update && apt-get install -y \
    apache2 \
    curl \
    git \
    libapache2-mod-php5 \
    php5 \
    php5-mcrypt \
    php5-mysql \
    python3.4

RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

RUN python3 get-pip.py    
RUN pip --version

RUN pip install bottle
RUN pip install elasticsearch-dsl
RUN pip install xlrd
RUN pip install requests

#ADD server.py /home/bottle/server.py
COPY src /home/bottle
WORKDIR /home/bottle

VOLUME /data

# in case you'd prefer to use links, expose the port
EXPOSE 8080

ENTRYPOINT ["/usr/bin/python3", "/home/bottle/index.py"]
# USER bottle
