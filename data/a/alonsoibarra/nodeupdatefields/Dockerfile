FROM debian:latest
MAINTAINER Saul ALonso Ibarra Luevano
RUN mkdir -p /opensource/
WORKDIR /opensource/
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install vim 
RUN apt-get -y install python-pip
RUN pip install nodejs
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*

RUN git clone https://github.com/AlonsoIbarra/NodeMysql.git
