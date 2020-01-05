FROM ubuntu:latest
MAINTAINER Andrew Husking (andrew@husking.id.au)
RUN apt-get update
RUN apt-get -y -q install curl apache2 libgd-graph-perl rrdtool dnsutils flow-tools wget vim

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV TZ=Australia/Canberra

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 80
