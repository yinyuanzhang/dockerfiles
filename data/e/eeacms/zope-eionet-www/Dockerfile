FROM eeacms/zope:2.13.26
MAINTAINER "European Environment Agency (EEA): IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>

ENV EVENT_LOG_LEVEL=INFO \
    Z2_LOG_LEVEL=INFO \
    ZEO_CLIENT=true \
    ZEO_ADDRESS=zeoserver:8100 \
    ZSERVER_THREADS=4 \
    BLOB_CACHE_SIZE=500000000 \
    SETUPTOOLS=33.1.1 \
    ZCBUILDOUT=2.9.5

COPY src/versions.cfg \
     src/sources.cfg \
     src/base.cfg $ZOPE_HOME/

RUN mkdir -p $ZOPE_HOME/products \
    && mkdir -p $ZOPE_HOME/var/log/ldap/log \
    && chown -R zope-www:zope-www $ZOPE_HOME/var/log/ldap \
    && mkdir -p $ZOPE_HOME/var/styles

RUN svn co https://svn.eionet.europa.eu/repositories/Zope/bundles/Eionet/trunk products

USER root

RUN mv /docker-entrypoint.sh /zope-entrypoint.sh

COPY entrypoint.sh /docker-entrypoint.sh


RUN ./install.sh \
    chown -R 500:500 $ZOPE_HOME

USER zope-www
