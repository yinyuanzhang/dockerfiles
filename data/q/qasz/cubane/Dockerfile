FROM ubuntu:16.04

# disable dialog tzdata
ENV DEBIAN_FRONTEND=noninteractive

# install initial requirements
RUN apt-get update && apt-get -y upgrade && apt-get autoremove && apt-get autoclean
RUN apt-get -y install python-minimal
RUN apt-get -y install python-pip
RUN apt-get -y install apt-utils
RUN apt-get -y install openjdk-8-jre
RUN apt-get -y install build-essential
RUN apt-get -y install python-dev
RUN apt-get -y install python-psycopg2
RUN apt-get -y install libmagickwand-dev
RUN apt-get -y install ghostscript
RUN apt-get -y install libjpeg-turbo-progs
RUN apt-get -y install optipng
RUN apt-get -y install net-tools
RUN apt-get -y install git
RUN apt-get -y install vim
RUN apt-get -y install postgresql
RUN apt-get -y install nginx
RUN apt-get -y install rsync
RUN apt-get -y install nfs-common
RUN apt-get -y install sshfs
RUN apt-get -y install postfix

# setup locales
RUN sed -i -e 's/# en_GB.UTF-8 UTF-8/en_GB.UTF-8 UTF-8/' /etc/locale.gen && locale-gen
ENV LANG en_GB.UTF-8
ENV LANGUAGE en_GB:en
ENV LC_ALL en_GB.UTF-8

# create cubane folder
WORKDIR /
RUN git clone https://github.com/cubaneorg/cubane.git
WORKDIR /cubane
RUN git checkout develop

# install cubane dependcies
RUN pip install --upgrade pip
RUN pip install -r /cubane/cubane/requirements/dev.txt
