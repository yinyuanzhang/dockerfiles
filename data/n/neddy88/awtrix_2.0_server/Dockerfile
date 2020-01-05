FROM	anapsix/alpine-java:8_jdk

RUN mkdir -p /data/ &&\
    cd /data/ &&\
    wget https://blueforcer.de/downloads/awtrix.jar
WORKDIR /data
VOLUME ["/data/config"]
VOLUME ["/data/plugins"]
ENTRYPOINT ["java", "-jar", "/data/awtrix.jar"]