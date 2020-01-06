FROM openjdk:8-jre

# Config and data
VOLUME /fuseki
ENV FUSEKI_BASE /fuseki

# Installation folder
ENV FUSEKI_HOME /jena-fuseki

ENV MAVEN_REPOSITORY https://repo.maven.apache.org/maven2
ENV PACKAGE_PATH org/apache/jena/apache-jena-fuseki
ENV FUSEKI_VERSION 3.9.0
#ENV FUSEKI_SHA1 449e976ba082d18e5018b173afc51ac73b6632aa

ENV BUILD_DEPS curl
ENV DEPS pwgen

# As "localhost" is often inaccessible within Docker container,
# we'll enable basic-auth with a random admin password 
# (which we'll generate on start-up)
COPY shiro.ini /jena-fuseki/shiro.ini
COPY shiro.ini /fuseki/shiro.ini

COPY docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh


WORKDIR /tmp
RUN mkdir -p $FUSEKI_HOME && \
    export DEBIAN_FRONTEND=noninteractive && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get update && \
    apt-get install -y $BUILD_DEPS $DEPS && \
    MAVEN_REPOSITORY_PATH=$MAVEN_REPOSITORY/$PACKAGE_PATH/$FUSEKI_VERSION && \
    FILE=apache-jena-fuseki-${FUSEKI_VERSION}.tar.gz && \
    URL=$MAVEN_REPOSITORY_PATH/$FILE && \
    echo Downloading $URL && \
    curl -f -O $URL && \
#echo $FUSEKI_SHA1 "" $FILE > $FILE.sha1 && \
#   cat $FILE.sha1 && \
#   sha1sum -c $FILE.sha1 && \ 
    tar -xzf $FILE && \
    rm apache-jena-fuseki-*/*war && \
    mv apache-jena-fuseki-*/* $FUSEKI_HOME && \
    apt-get remove -y --purge $BUILD_DEPS && \
    apt-get autoremove -y && \
    apt-get autoclean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/*

COPY fuseki_overrides/ /jena-fuseki/
RUN chmod 755 /jena-fuseki/run.sh

COPY load.sh /jena-fuseki/
COPY tdbloader /jena-fuseki/
RUN chmod 755 /jena-fuseki/load.sh /jena-fuseki/tdbloader

# Where we start our server from
WORKDIR /jena-fuseki
EXPOSE 3030
#ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["cd jena-fuseki"]
CMD ["./run.sh"]

#ENTRYPOINT /bin/bash
