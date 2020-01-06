FROM openjdk:8-jre

# Based on the original by Andrew Grande.  See aperepel/nifi
MAINTAINER Uday Kabe <uday.kabe@exolyte.com>

ENV NIFI_VERSION=1.2.0

RUN wget -q https://archive.apache.org/dist/nifi/$NIFI_VERSION/nifi-$NIFI_VERSION-bin.tar.gz && \
    tar zxf nifi*.tar.gz && \
    rm -f nifi*.tar.gz

VOLUME ["/output", "/flowconf", "/flowrepo",  "/contentrepo", "/databaserepo", "/provenancerepo"]

ENV NIFI_HOME=/nifi-$NIFI_VERSION

# web port
EXPOSE 8080

# listen port for web listening processor
EXPOSE 8081

# additional ports for user apps (bind them in a docker-compose.yml 'ports' section)
EXPOSE 10000 10001 10002 10003 10004

WORKDIR $NIFI_HOME/bin

ADD ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

CMD ["./nifi.sh", "run"]
