FROM faboulaye/openjdk:latest
MAINTAINER Firdaws Aboulaye "aboufred@gmail.com"

ENV NEO4J_HOME /var/lib/neo4j

# Install
RUN groupadd -r neo4j \
  && useradd -r -g neo4j neo4j \
  && apt-get update \
  && apt-get install wget -y \
  && wget -O - https://debian.neo4j.org/neotechnology.gpg.key | apt-key add - \
  && echo 'deb http://debian.neo4j.org/repo stable/' > /tmp/neo4j.list \
  && mv /tmp/neo4j.list /etc/apt/sources.list.d \
  && apt-get update \
  && apt-get install --no-install-recommends -y neo4j \
  && sed -e 's/^#dbms.connector.http.address=0.0.0.0:7474/dbms.connector.http.address=0.0.0.0:7474/' -i /etc/neo4j/neo4j.conf \
  && apt-get remove -y wget \
  && apt-get clean \
  && rm -rf /tmp/* /usr/share/man/?? /usr/share/man/??_* /var/lib/apt/lists/*

USER neo4j
VOLUME $NEO4J_HOME/data
EXPOSE 7474 7473 7687

CMD ["bash"]
