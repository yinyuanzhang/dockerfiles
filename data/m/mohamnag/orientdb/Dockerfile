# orientdb
FROM java:8
LABEL "maintainer"="Mohammad Naghavi <mohamnag@gmail.com>"
LABEL "updated"="Aranga C. Nanayakkara <aranga.nanayakkara@gmail.com"
LABEL "updated-date"="2019-09-05"

ARG ORIENTDB_DOWNLOAD_SERVER

ENV ORIENTDB_VERSION 3.0.23
ENV ORIENTDB_DOWNLOAD_MD5 54f3badc3aff39e27331be3371c4e7d8
ENV ORIENTDB_DOWNLOAD_SHA1 63e3cd3082bc7a8a55a136e991560e39a3f1a709

ENV ORIENTDB_URL ${ORIENTDB_DOWNLOAD_SERVER:-http://central.maven.org/maven2/com/orientechnologies}/orientdb-tp3/$ORIENTDB_VERSION/orientdb-tp3-$ORIENTDB_VERSION.tar.gz

# env variables that best be changed by run command
ENV ORIENTDB_ROOT_PASSWORD=changeme
ENV HEAP_MEM_LIMIT=4g
ENV DISK_CACHE_BUFFER=1536
ENV ODB_NETWORK_LOCKTIMEOUT=30000
ENV ODB_NETWORK_SOCKETTIMEOUT=30000

# install orientdb
ENV ORIENTDB_HOME='/opt/orientdb'

ADD ${ORIENTDB_URL} /tmp/orientdb.tar.gz

RUN mkdir -p ${ORIENTDB_HOME} \ 
    && tar -zxvf /tmp/orientdb.tar.gz --strip-components=1 --directory ${ORIENTDB_HOME} \
    && ln -s ${ORIENTDB_HOME}/bin/* /usr/local/bin/ \
    && rm -rf /tmp/ \
    && rm -rf ${ORIENTDB_HOME}/databases/ \
    && mkdir /usr/local/log

ADD service.sh ${ORIENTDB_HOME}/
RUN chmod +x ${ORIENTDB_HOME}/service.sh
VOLUME ${ORIENTDB_HOME}/databases/

# configure system
EXPOSE 2424
EXPOSE 2480

WORKDIR ${ORIENTDB_HOME}

ENTRYPOINT ["./service.sh"]

