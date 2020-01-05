FROM centos:7

MAINTAINER Abed Halawi <abed.halawi@vinelab.com>

# Make sure we're running the latest stuff
RUN yum -y update

# Install basic software
RUN yum install -y rsyslog cronie vim wget tar

# Add epel repo
RUN yum -y install http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm

# Install & configure supervisord
RUN yum -y install python-setuptools
RUN easy_install supervisor
RUN /usr/bin/echo_supervisord_conf > /etc/supervisord.conf
RUN mkdir -p /var/log/supervisord

# Make supervisor run in foreground
RUN sed -i -e "s/^nodaemon=false/nodaemon=true/" /etc/supervisord.conf

# Make supervisor run the http server on 9001
RUN sed -i -e "s/^;\[inet_http_server\]/\[inet_http_server\]/" /etc/supervisord.conf
RUN sed -i -e "s/^;port=127.0.0.1:9001/port=0.0.0.0:9001/" /etc/supervisord.conf
# tell supervisor to include relative .ini files
RUN echo [include] >> /etc/supervisord.conf
RUN echo 'files = /etc/supervisord.d/*.ini' >> /etc/supervisord.conf

# add programs to supervisord config
RUN mkdir /etc/supervisord.d
ADD ini/rsyslog.ini /etc/supervisord.d/rsyslog.ini
ADD ini/cron.ini /etc/supervisord.d/cron.ini

# cleanup installation stuff
RUN yum clean all

# Setup locale
RUN echo 'LANG=C' > /etc/sysconfig/i18n

ADD init.sh /
RUN chmod +x /init.sh

# EXPOSE 9001

CMD /init.sh
