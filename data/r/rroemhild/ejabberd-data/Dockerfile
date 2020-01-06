FROM busybox
MAINTAINER Rafael Römhild <rafael@roemhild.de>

ENV EJABBERD_USER ejabberd
ENV EJABBERD_HOME /opt/ejabberd

RUN mkdir -p $EJABBERD_HOME/database \
    $EJABBERD_HOME/ssl \
    $EJABBERD_HOME/backup \
    $EJABBERD_HOME/upload \
  && chown -R 999:999 $EJABBERD_HOME

VOLUME ["$EJABBERD_HOME/database", "$EJABBERD_HOME/ssl", "$EJABBERD_HOME/backup", "$EJABBERD_HOME/upload"]
