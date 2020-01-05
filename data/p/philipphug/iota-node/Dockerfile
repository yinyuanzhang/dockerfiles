FROM maven:3.5-jdk-8

WORKDIR /iri

RUN git clone -b v1.4.0 https://github.com/iotaledger/iri.git /iri/
RUN mvn -q clean package

COPY logback.xml /iri/
COPY /docker-entrypoint.sh /

WORKDIR /iri/data

VOLUME /iri/data

EXPOSE 14265
EXPOSE 14777/udp
EXPOSE 15777

ENTRYPOINT ["/docker-entrypoint.sh"]

