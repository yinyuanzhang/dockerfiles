############################################################
# Dockerfile to build supervisor container image
# based on phusion/baseimage
############################################################
# Basis Image Ubuntu 16.04
############################################################

# Set the base Image
FROM phusion/baseimage:0.10.2

# File Author / Maintainer
MAINTAINER Sven Berger

############################################################
# RUN INSTALL AS root
############################################################

USER root

############################################################
# don't ask for stupid things
############################################################

ENV DEBIAN_FRONTEND noninteractive
RUN echo APT::Install-Recommends "0"; >> /etc/apt/apt.conf
RUN echo APT::Install-Suggests "0"; >> /etc/apt/apt.conf

############################################################
# Environment Variables
############################################################

ENV LC_ALL de_DE.UTF-8
ENV LANG de_DE.UTF-8
ENV LANGUAGE de_DE.UTF-8
ENV USERNAME ubuntu
ENV USERID 2000
ENV GROUPID 2000
ENV TZ Europe/Berlin

############################################################
# Update Repository and upgrade Software
############################################################

COPY install/sources.list /etc/apt/sources.list
RUN apt-get update; \
apt-get install apt-utils locales ubuntu-extras-keyring -y; \
apt-get update

############################################################
# Konfigure timezone and locale
############################################################

RUN locale-gen $LC_ALL
COPY install/default_locale /etc/default/locale
RUN chmod 0755 /etc/default/locale
RUN apt-get install language-pack-de language-pack-de-base -y &&  apt-get purge language-pack-en language-pack-en-base -y
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

############################################################
# Container Users
############################################################

RUN addgroup --gid $GROUPID $USERNAME
RUN adduser --uid $USERID --gid $GROUPID --disabled-login --no-create-home --disabled-password $USERNAME

############################################################
# Add Software Repositories
############################################################

############################################################
# Add Software and Upgrade
############################################################

RUN apt-get update; \
apt-get install wget nano mc tzdata -y; \
apt-get dist-upgrade -y

############################################################
# Begin Installation
############################################################

RUN apt-get update; \
apt-get dist-upgrade -y

############################################################
# Backup installed Config
############################################################

############################################################
# Copy Files
############################################################

############################################################
# Remove Apt Data
############################################################

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

############################################################
# Container RUN USER
############################################################

USER $USERNAME

############################################################
# Ports needed
############################################################

############################################################
# Ports needed by App
############################################################

############################################################
# Folders needed
############################################################

############################################################
# Container Start
############################################################
