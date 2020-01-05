#
# Dockerizing Neo4j graph database (http://www.github.com/kbastani/docker-neo4j)
#
FROM       dockerfile/java:oracle-java8
MAINTAINER K.B. Name <kb@socialmoon.com>

# Install Neo4j
RUN wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add - && \
    echo 'deb http://debian.neo4j.org/repo stable/' > /etc/apt/sources.list.d/neo4j.list && \
    apt-get update ; apt-get install neo4j -y

WORKDIR /etc/neo4j

# Copy graph analytics plugin
COPY plugins /var/lib/neo4j/plugins

# Copy configurations
COPY conf/neo4j /var/lib/neo4j/conf

# Copy the bootstrap shell script and set permissions
COPY sbin/bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh && \
    chmod 700 /etc/bootstrap.sh

# Customize configurations
RUN apt-get clean && \
    sed -i "s|data/graph.db|/opt/data/graph.db|g" /var/lib/neo4j/conf/neo4j-server.properties && \
    sed -i "s|#org.neo4j.server.webserver.address|org.neo4j.server.webserver.address|g" /var/lib/neo4j/conf/neo4j-server.properties && \
    sed -i "s|#org.neo4j.server.thirdparty_jaxrs_classes=org.neo4j.examples.server.unmanaged=/examples/unmanaged|org.neo4j.server.thirdparty_jaxrs_classes=extension=/service,com.nigelsmall.load2neo=/load2neo|g" /var/lib/neo4j/conf/neo4j-server.properties

# Expose the Neo4j browser to the host OS on port 7474 and 1337
EXPOSE 7474
EXPOSE 1337

# Set the bootstrap script on container run
ENV BOOTSTRAP /etc/bootstrap.sh
CMD ["/etc/bootstrap.sh", "-d"]
