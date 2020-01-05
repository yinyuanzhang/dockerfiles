FROM linuxserver/baseimage.python

MAINTAINER hernando
# set python to use utf-8 rather than ascii
ENV PYTHONIOENCODING="UTF-8"

# install pip packages
RUN pip install mako && \
apt-get clean && rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*

# Adding Custom files
ADD init/ /etc/my_init.d/
ADD services/ /etc/service/

RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh

# Volumes and Ports
VOLUME /config /downloads /tv
EXPOSE 8081

#ADD cron/ /etc/cron.d/
#RUN chmod 0644 /etc/cron.d/cronjob



