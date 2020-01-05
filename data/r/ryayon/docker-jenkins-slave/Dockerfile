FROM ryayon/docker-jenkins-slave:centos7
MAINTAINER Rudy YAYON <ryayon@outlook.com>

RUN ln -sf /usr/share/zoneinfo/Europe/Paris /etc/localtime

####################################### Install svn 1.9 binary for maven release on svn ###################################
COPY ./wandisco-svn.repo /etc/yum.repos.d/wandisco-svn.repo
RUN yum -y install subversion \
&& yum clean all

####################################### tar and bzip2 for npm packages compilation ########################################
RUN yum clean all && yum -y install \
    tar \
    bzip2 \
&& yum clean all

############################################### Selenium and firefox-44.0.1 ###############################################
RUN yum clean all && yum -y install \
    xorg-x11-server-Xvfb \
    dbus \
    gtk+-devel \
    glib-devel \
    pango \
    libstdc++ \
    libstdc++-devel \
    lbzip2 \
    gtk2 \
    wget \
&& yum clean all

RUN wget -q https://download-installer.cdn.mozilla.net/pub/firefox/releases/44.0.1/linux-x86_64/fr/firefox-44.0.1.tar.bz2 \
    && tar xf firefox-44.0.1.tar.bz2 -C /usr/local/ \
    && ln -s /usr/local/firefox/firefox /usr/bin/firefox

RUN dbus-uuidgen > /var/lib/dbus/machine-id
RUN dbus-uuidgen > /etc/machine-id
###########################################################################################################################
