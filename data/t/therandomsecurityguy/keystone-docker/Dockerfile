FROM ubuntu:14.04

MAINTAINER Derek Chamorro <therandomsecurityguy at gmail dot com>

# Update and install keystone and supervisor
RUN apt-get -y update && apt-get install -y --no-install-recommends \
  mysql-client \
  keystone \
  python-keystoneclient \
  python-memcache \
  python-mysqldb \
  supervisor \
  && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Run keystone with supervisord
COPY supervisord/supervisord-keystone.conf /etc/supervisor/conf.d/supervisord-keystone.conf

# Restart supervisord
RUN service supervisor start

EXPOSE 35357 5000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf", "-n"]
