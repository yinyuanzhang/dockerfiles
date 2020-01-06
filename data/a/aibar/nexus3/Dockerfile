FROM iron/java:1.8

ENV RUN_AS_USER=root

WORKDIR /

RUN wget http://download.sonatype.com/nexus/3/nexus-3.0.0-03-unix.tar.gz -O nexus.tar.gz && \
    tar -xzvf nexus.tar.gz && \
    rm nexus.tar.gz

COPY nexus.vmoptions /nexus-3.0.0-03/bin

VOLUME /data

EXPOSE 8081

ENTRYPOINT ["/nexus-3.0.0-03/bin/nexus", "run"]
