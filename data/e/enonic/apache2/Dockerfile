
# Base image
FROM ubuntu:14.04

MAINTAINER Erik Kaareng-Sunde esu@enonic.com

#### Inspired by the tianon/apache2 image ####

RUN apt-get update && apt-get install -y apache2 rsync git

# let's copy a few of the settings from /etc/init.d/apache2
ENV APACHE_CONFDIR /etc/apache2
ENV APACHE_ENVVARS $APACHE_CONFDIR/envvars
# and then a few more from $APACHE_CONFDIR/envvars itself
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_PID_FILE $APACHE_RUN_DIR/apache2.pid
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_LOG_DIR /var/log/apache2
ENV LANG C

# ...
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR

# make CustomLog (access log) go to stdout instead of files
#  and ErrorLog to stderr
RUN find "$APACHE_CONFDIR" -type f -exec sed -ri ' \
    s!^(\s*CustomLog)\s+\S+!\1 /proc/self/fd/1!g; \
    s!^(\s*ErrorLog)\s+\S+!\1 /proc/self/fd/2!g; \
' '{}' ';'


#### End tianon/apache2 base ####

ADD scripts/gen_proxy_conf /usr/local/bin/gen_proxy_conf
RUN chmod +x /usr/local/bin/gen_proxy_conf

ADD scripts/rm_vhost_conf /usr/local/bin/rm_vhost_conf
RUN chmod +x /usr/local/bin/rm_vhost_conf

ADD scripts/sync_static_files /usr/local/bin/sync_static_files
RUN chmod +x /usr/local/bin/sync_static_files

ADD scripts/gen_linking_proxy_conf /usr/local/bin/gen_linking_proxy_conf
RUN chmod +x /usr/local/bin/gen_linking_proxy_conf

ADD scripts/deploy_linking_proxy_conf /usr/local/bin/deploy_linking_proxy_conf
RUN chmod +x /usr/local/bin/deploy_linking_proxy_conf

ADD scripts/reload_apache2 /usr/local/bin/reload_apache2
RUN chmod +x /usr/local/bin/reload_apache2

ADD scripts/enable_proxy_modules /usr/local/bin/enable_proxy_modules
RUN chmod +x /usr/local/bin/enable_proxy_modules

ADD scripts/launcher.sh /usr/local/bin/launcher.sh
RUN chmod +x /usr/local/bin/launcher.sh

VOLUME /etc/apache2 /etc/ssl /var/log/apache2 /var/www/html

EXPOSE 80 443

CMD launcher.sh
