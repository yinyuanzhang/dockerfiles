# bioinformatics tools base image
#
# 2014/06/30
#
FROM ubuntu:12.04
MAINTAINER Mario Fasold "mario.fasold@ecseq.com"

# RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list

RUN apt-get -qq update

## basic tools
RUN apt-get install -y wget zip unzip python-setuptools rsync

## install java & and remove unessary stuff in one go
RUN (apt-get install -y python-software-properties; \
     add-apt-repository -y ppa:webupd8team/java; \
     apt-get update  -y; \
     echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections; \
     apt-get install -y oracle-java7-installer; \
     apt-get remove -y --purge python-software-properties; \
     apt-get autoremove -y; \
     apt-get clean -y)

# install perl & python tools
RUN apt-get install -y libyaml-perl  libtemplate-perl python-biopython libjson-perl python-yaml libpar-packer-perl 

# install ruby & gems for bioruby
RUN apt-get install -y ruby-dev rubygems

# install libraris needed by NGS tools
RUN apt-get install -y tabix libncurses5-dev
