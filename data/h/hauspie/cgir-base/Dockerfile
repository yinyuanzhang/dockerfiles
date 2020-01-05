FROM debian:jessie

MAINTAINER michael.hauspie@univ-lille1.fr

RUN apt-get update && apt-get install --yes --force-yes vim less man-db manpages manpages-dev runit rsyslog


# Create rsyslogd service
RUN mkdir -p /var/run/rsyslogd
RUN mkdir /etc/service/rsyslogd
RUN /bin/echo -e '#!/bin/sh' > /etc/service/rsyslogd/run
RUN /bin/echo -e 'exec /usr/sbin/rsyslogd -n' >> /etc/service/rsyslogd/run
RUN chown root.root /etc/service/rsyslogd/run
RUN chmod 755 /etc/service/rsyslogd/run


ENTRYPOINT ["/usr/sbin/runsvdir-start"]

