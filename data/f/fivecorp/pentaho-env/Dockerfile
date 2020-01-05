FROM openjdk:8-jdk-stretch

MAINTAINER fivecorp

# Install dependencies.
#
# - xvfb to support headless reports
# - wget, build-essential et al to build apr, tomcat-native, etc.
#
# Add pentaho user and group
#
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      xvfb wget build-essential openssl unzip libssl-dev postgresql-client && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    groupadd -g 1000 pentaho && \
    useradd  -g pentaho -u 1000 -m pentaho && \
    mkdir /opt/scratch && \
    chown pentaho:pentaho /opt/scratch

# Get this version from https://apr.apache.org/download.cgi
ENV APR_VERSION 1.7.0
RUN cd /tmp && \
    wget "http://apache.rediris.es/apr/apr-${APR_VERSION}.tar.bz2" && \
    tar -xjvf "apr-${APR_VERSION}.tar.bz2" && \
    cd "apr-${APR_VERSION}" && \
    ./configure --prefix=/usr && \
    make && \
    make install && \
    rm -rf /tmp/*

# Get this version from https://tomcat.apache.org/download-native.cgi
ENV TCN_VERSION 1.2.23
RUN cd /tmp && \
    wget "http://apache.rediris.es/tomcat/tomcat-connectors/native/${TCN_VERSION}/source/tomcat-native-${TCN_VERSION}-src.tar.gz" && \
    tar -xzvf "tomcat-native-${TCN_VERSION}-src.tar.gz" && \
    cd "tomcat-native-${TCN_VERSION}-src/native" && \
    ./configure --prefix=/usr --with-apr=/usr \
        --with-java-home=$JAVA_HOME && \
    make && \
    make install && \
    rm -rf /tmp/*

# C3P0 connection pool from  https://sourceforge.net/projects/c3p0/
ENV C3P0_VERSION 0.9.5.4
RUN cd /tmp && \
    wget "https://sourceforge.net/projects/c3p0/files/c3p0-bin/c3p0-${C3P0_VERSION}/c3p0-${C3P0_VERSION}.bin.tgz/download" && \
    mv download "c3p0-${C3P0_VERSION}.tgz" && \
    tar -xzvf "c3p0-${C3P0_VERSION}.tgz" && \
    mv c3p0-${C3P0_VERSION}/lib/* /usr/local/lib && \
    rm -rf /tmp/*

# Get this version from https://logging.apache.org/log4j/
ENV LOG4J_EXTRAS_VERSION 1.2.17
RUN cd /tmp && \
    wget "http://apache.rediris.es/logging/log4j/extras/${LOG4J_EXTRAS_VERSION}/apache-log4j-extras-${LOG4J_EXTRAS_VERSION}-bin.tar.gz" && \
    tar -xzvf "apache-log4j-extras-${LOG4J_EXTRAS_VERSION}-bin.tar.gz" && \
    mv "apache-log4j-extras-${LOG4J_EXTRAS_VERSION}/apache-log4j-extras-${LOG4J_EXTRAS_VERSION}.jar" /usr/local/lib && \
    rm -rf /tmp/*

# Get this version from https://dev.mysql.com/downloads/connector/j/
ENV MYSQL_CONN_VERSION 8.0.17
RUN cd /tmp && \
    wget "https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-${MYSQL_CONN_VERSION}.tar.gz" && \
    tar -xzvf "mysql-connector-java-${MYSQL_CONN_VERSION}.tar.gz" && \
    mv "mysql-connector-java-${MYSQL_CONN_VERSION}/mysql-connector-java-${MYSQL_CONN_VERSION}.jar" /usr/local/lib && \
    rm -rf /tmp/*

# Get this version from https://jdbc.postgresql.org/download.html
ENV PGSQL_CONN_VERSION 42.2.6
RUN cd /tmp && \
    wget "https://jdbc.postgresql.org/download/postgresql-${PGSQL_CONN_VERSION}.jar" && \
    mv "postgresql-${PGSQL_CONN_VERSION}.jar" /usr/local/lib

# Hazelcast CDC cache from https://github.com/webdetails/cdc
ENV CDC_VERSION 18.04.05
RUN cd /tmp && \
    wget "https://github.com/webdetails/cdc/releases/download/${CDC_VERSION}/cdc-pentaho5-redist-${CDC_VERSION}.zip" && \
    mkdir -p /usr/local/src/hazelcast && \
    cd /usr/local/src/hazelcast && \
    unzip /tmp/cdc-pentaho5-redist-${CDC_VERSION}.zip && \
    chmod 0755 launch-hazelcast.sh && \
    rm -rf /tmp/*

# Set environment variables for Pentaho
ENV JAVA_VERSION 8
ENV PENTAHO_JAVA_HOME "/usr/local/openjdk-8"
ENV PENTAHO_JAVA "/usr/local/openjdk-8/bin/java"

# Add tini
ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini
ENTRYPOINT ["/tini", "--"]

# Pentaho must be downloaded, uncompressed and mounted as a volume in the path /opt/biserver-ce.
#
# Pentaho can be downloaded from:
# http://downloads.sourceforge.net/project/pentaho/Business Intelligence Server/${PENTAHO_MAJOR}/biserver-ce-${PENTAHO_MINOR}.zip

VOLUME  /opt/pentaho-server
WORKDIR /opt/pentaho-server
ENV PENTAHO_HOME "/opt/pentaho-server"

# If this instance is to be run behind a proxy, the proxy port and
# scheme must be given as environment variables, e.g.
ENV PENTAHO_PORT 8080
ENV PROXY_PORT 8080
ENV PROXY_SCHEME http

# Configuration files from Pentaho 8.3
ADD files /opt/

# Pentaho port
USER   pentaho
EXPOSE 8080

CMD "/opt/start.sh"

