FROM debian:stretch-slim
LABEL maintainer="EEA: IDM2 A-Team <eea-edw-a-team-alerts@googlegroups.com>"

ENV CYNIN_PATH /var/local
ENV CYNIN_BUILDOUT https://svn.eionet.europa.eu/repositories/Zope/trunk/community.eea.europa.eu/tags/2.5
ENV CYNIN_NAME community.eea.europa.eu
ENV INSTANCEDIR $CYNIN_PATH/$CYNIN_NAME

RUN groupadd -g 500 cynin \
 && mkdir -p $INSTANCEDIR \
 && useradd cynin -d $INSTANCEDIR -u 500 -g cynin \
 && chown -R cynin:cynin $INSTANCEDIR

COPY install.sh /tmp/
RUN apt-get update \
 && apt-get -y  install ca-certificates git wget gcc build-essential subversion cron gosu nano \
    libblas-dev \
    libc6-dev \
    libexpat1-dev \
    libjpeg-dev  \
    liblapack-dev \
    libldap2-dev \
    libmemcached-dev \
    libpq-dev \
    libreadline-dev \
    libsasl2-dev  \
    libssl-dev \
    libxml2-dev \
    libxmlsec1-dev  \
    libxslt-dev \
    libxslt1-dev \
    libz-dev \
    zlib1g-dev \
    libfreetype6 \
    libfreetype6-dev \
 && apt-get -y install libssl1.0-dev libjpeg62 libpng16-16  librsvg2-bin \
 && mkdir /opt/python-2.4 \
 && cd /tmp \
 && wget https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz \
 && tar zxf Python-2.4.6.tgz \
 && cd Python-2.4.6 \
 && find / -name *ssl \
 && grep -i ssl Modules/Setup.dist \
 && sed -i '/_ssl/s/^#//g' Modules/Setup.dist \
 && sed -i '/DUSE_SSL/s/^#//g' Modules/Setup.dist \
 && sed -i '/lssl/s/^#//g' Modules/Setup.dist \
 && grep -i ssl Modules/Setup.dist \
 && ./configure --with-zlib=/usr/include --prefix=/opt/python-2.4 --enable-ipv6 \
 && sed -i "s/^#zlib/zlib/g" Modules/Setup \
 && make \
 && make install \
 && ls /opt/python-2.4/bin \
 && ln -s  /opt/python-2.4/bin/python2.4 //usr/local/bin/python2.4 \
 && cd $INSTANCEDIR \
 && svn co $CYNIN_BUILDOUT . \
 && mv /tmp/install.sh . \
 && ./install.sh \
 && ./bin/buildout -c deploy.cfg \
 && touch var/log/event.log \
 && chown -R cynin:cynin $INSTANCEDIR \
 && apt-get remove -y --purge git subversion gcc build-essential zlib1g-dev libssl-dev libxmlsec1-dev \
 && apt-get autoremove -y \
 && apt-get autoclean \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 8080
WORKDIR $INSTANCEDIR
USER root

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["start"]
