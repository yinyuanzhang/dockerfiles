FROM centos:centos7

MAINTAINER The Atlantic Programmers <programmers@theatlantic.com>
ARG BUILD_DATE
ARG VERSION
ARG VCS_REV
ENV VCS_URL git@github.com:theatlantic/ollie-docker-containers.git

LABEL org.label-schema.name="ollie-centos7" \
      org.label-schema.description="Ollie CentOS 7 base container" \
      org.label-schema.vendor="The Atlantic" \
      org.label-schema.version="$VERSION" \
      org.label-schema.vcs-url="$VCS_URL" \
      org.label-schema.license="BSD-2" \
      org.label-schema.schema-version="1.2"

# Allow scripts to detect we're running in our own container
RUN touch /ollie-centos7-container

# add our user and group first to make sure their IDs get assigned
# consistently, regardless of whatever dependencies get added
RUN groupadd -g 509 deploy && useradd -m -u 508 -g 509 -G deploy deploy

# Set the locale.
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN cd /usr/lib/locale \
    && localedef --list-archive | grep -v -i ^en \
        | xargs localedef --delete-from-archive \
    && localedef -i en_US -f UTF-8 en_US.UTF-8 \
    && mv -f locale-archive locale-archive.tmpl \
    && build-locale-archive

ENV THEATLANTIC_RELEASE_RPM "http://dev.theatlantic.com/repo/el/7/x86_64/"\
"packages/theatlantic-release-7-1.noarch.rpm"

# Use openshift epel mirror, because it doesn't have constant syncing
# race-condition errors
RUN curl -SLv -o /etc/yum.repos.d/epel7.repo https://mirror.openshift.com/mirror/epel/epel7.repo

# Include docs!
RUN sed -i '/tsflags=nodocs/d' /etc/yum.conf

RUN yum update -y --setopt=tsflags= \
 && yum install -y --setopt=tsflags= "${THEATLANTIC_RELEASE_RPM}" \
 && yum clean all

RUN yum install -y https://rpm.nodesource.com/pub_10.x/el/7/x86_64/nodesource-release-el7-1.noarch.rpm \
  && yum clean all

# add gosu for easy step-down from root
ENV GOSU_VERSION 1.10

RUN yum update -y --setopt=tsflags= \
 && yum install -y --setopt=tsflags= dpkg \
 && curl -SLv -o /usr/bin/gosu \
  "https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg --print-architecture)" \
 && chmod +x /usr/bin/gosu \
 && /usr/bin/gosu nobody true \
 && yum erase -y dpkg \
 && yum clean all

ENV DOCKERIZE_VERSION 0.3.0

RUN curl -SL \
"https://github.com/jwilder/dockerize/releases/download/v$DOCKERIZE_VERSION/"\
"dockerize-linux-amd64-v$DOCKERIZE_VERSION.tar.gz" \
    | tar -xzC /usr/bin

# Assorted utilities
RUN yum update -y --setopt=tsflags= \
 && yum install -y --setopt=tsflags= \
  which \
  sudo \
  git \
  git-crypt \
  man \
  man-pages \
  nano \
  emacs-nox \
  telnet \
  nc \
  lsof \
  perl \
  openssh-clients \
  bzip2 \
  bash-completion \
  curl \
  wget \
  rsync \
 && yum clean all \
 && cd /usr/lib/locale \
 && localedef --list-archive | grep -v -i ^en | xargs localedef --delete-from-archive \
 && localedef -i en_US -f UTF-8 en_US.UTF-8 \
 && mv -f locale-archive locale-archive.tmpl \
 && build-locale-archive

# Set TZ
RUN ln -fs /usr/share/zoneinfo/America/New_York /etc/localtime

# Configure bash history.
ENV HISTSIZE 50000
ENV HISTIGNORE ls:exit:"cd .."

# This prevents dupes but only in memory for the current session.
ENV HISTCONTROL erasedups

ADD sudoers-deploy /etc/sudoers.d/deploy

RUN mkdir /docker-entrypoint-initdb.d

RUN mkdir -p /mnt/{home,vols} && chown -R deploy:deploy /mnt

VOLUME ["/mnt/home", "/mnt/vols"]

ADD ps1.sh /etc/profile.d/ps1.sh

LABEL org.label-schema.build-date="$BUILD_DATE" \
      org.label-schema.vcs-rev="$VCS_REV"
