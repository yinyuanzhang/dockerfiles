FROM aibar/jvm:1.8

EXPOSE 8081

VOLUME /data

ENV RUN_AS_USER=root

ENTRYPOINT ["/nexus-2.14.1-01/bin/nexus", "console"]

RUN wget http://dl.bintray.com/walkingdevs/mirrors/nexus-2.14.1-01.tar.gz \
         -O nexus.tar.gz && \
    tar xfv nexus.tar.gz && \
    rm nexus.tar.gz

COPY nexus.properties /nexus-2.14.1-01/conf