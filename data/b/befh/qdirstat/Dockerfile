FROM hurricane/dockergui:x11rdp

MAINTAINER Brian Fulton-Howard

## Based on coppit/docker-filebot

ENV APP_NAME="QDirStat" WIDTH=1280 HEIGHT=720 TERM=xterm

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

ENV DEBIAN_FRONTEND=noninteractive
ADD dpkg-excludes /etc/dpkg/dpkg.cfg.d/excludes

RUN \

# Speed up APT
echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup && \
echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache

# Add QDirStat Repository
RUN add-apt-repository -y ppa:nathan-renniewaldock/qdirstat

# Update apt and install dependencies.
RUN apt-get update -q

# Install QDirStat
RUN apt-get install --no-install-recommends -qy --force-yes qdirstat

RUN \

# Revision-lock to a specific version to avoid any surprises.
wget -q -O /runas.sh \
  'https://raw.githubusercontent.com/coppit/docker-inotify-command/c9e9c8b980d3a5ba4abfe7c1b069f684a56be6d2/runas.sh' && \
chmod +x /runas.sh && \

# clean up
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
/usr/share/man /usr/share/groff /usr/share/info \
/usr/share/lintian /usr/share/linda /var/cache/man && \
(( find /usr/share/doc -depth -type f ! -name copyright|xargs rm || true )) && \
(( find /usr/share/doc -empty|xargs rmdir || true ))

VOLUME "/host"

ENV USER_ID 0
ENV GROUP_ID 0
ENV UMASK 0000

EXPOSE 3389 8080

# Set the locale, to support files that have non-ASCII characters
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

COPY startapp.sh /

RUN \

# Fix guacamole errors and warnings:
# SEVERE: The scratchDir you specified: /var/lib/tomcat7/work/Catalina/localhost/guacamole is unusable.
# SEVERE: Cannot find specified temporary folder at /tmp/tomcat7-tomcat7-tmp
# WARNING: Failed to create work directory [/var/lib/tomcat7/work/Catalina/localhost/_] for context []
mkdir -p /var/cache/tomcat7 /tmp/tomcat7-tomcat7-tmp /var/lib/tomcat7/work/Catalina/localhost && \
ln -s /var/lib/tomcat7/common /usr/share/tomcat7/common && \
ln -s /var/lib/tomcat7/server /usr/share/tomcat7/server && \
ln -s /var/lib/tomcat7/shared /usr/share/tomcat7/shared

RUN mkdir /etc/service/qdirstat
ADD startapp.sh /etc/service/qdirstat/run
RUN chmod +x /etc/service/qdirstat/run
