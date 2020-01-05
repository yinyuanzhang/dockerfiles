FROM ubuntu:bionic
MAINTAINER Albert Alvarez

#RUN locale-gen es_ES.UTF-8
ENV LANG='es_ES.UTF-8' LANGUAGE='es_ES:es' LC_ALL='es_ES.UTF-8'

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install software-properties-common -y

RUN add-apt-repository -y ppa:libreoffice/ppa
RUN apt-get update
RUN apt-get install -y libreoffice

RUN apt-get remove libreoffice-gnome -y




CMD libreoffice
