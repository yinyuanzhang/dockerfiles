FROM marvambass/apache2-ssl-php
MAINTAINER MarvAmBass

ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y \
    subversion \
    libapache2-svn \
    apache2-mpm-prefork

RUN a2enmod dav_svn
RUN a2enmod auth_digest

RUN mkdir /var/svn-backup
RUN mkdir -p /var/local/svn
RUN mkdir /etc/apache2/dav_svn
RUN mkdir /etc/apache2/custom-conf

ADD files/dav_svn.conf /etc/apache2/mods-available/dav_svn.conf

ADD files/svn-backuper.sh /usr/local/bin/
ADD files/svn-project-creator.sh /usr/local/bin/
ADD files/svn-entrypoint.sh /usr/local/bin/

RUN chmod a+x /usr/local/bin/svn*

RUN echo "*/10 * * * *	root    /usr/local/bin/svn-project-creator.sh" >> /etc/crontab

RUN sed -i 's/# exec CMD/&\nsvn-entrypoint.sh/g' /opt/entrypoint.sh

VOLUME ["/var/local/svn", "/etc/apache2/dav_svn", "/etc/apache2/custom-conf"]
