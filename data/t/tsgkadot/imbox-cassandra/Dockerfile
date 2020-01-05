FROM java:8-jdk-alpine

MAINTAINER tsgkdt <tsgkadot@gmail.com>
ENV CASSANDRA_VER 1.1.12

# Install Cassandra
RUN apk add --no-cache libc6-compat bash && \
    apk add --virtual=dependencies --no-cache wget unzip && \
    wget http://archive.apache.org/dist/cassandra/${CASSANDRA_VER}/apache-cassandra-${CASSANDRA_VER}-bin.tar.gz && \
    tar xvzf apache-cassandra-${CASSANDRA_VER}-bin.tar.gz -C /usr/local && \
    ln -s /usr/local/apache-cassandra-1.1.12 /usr/local/cassandra && \
    rm -f apache-cassandra-${CASSANDRA_VER}-bin.tar.gz

# Copy files
COPY ./config/* /usr/local/cassandra/conf/
COPY entrypoint.sh /usr/local/cassandra/

# Authentication Settings
RUN wget http://www.intra-mart.jp/download/product/iap/imbox/cassandra_simple_auth.zip && \
    unzip cassandra_simple_auth.zip -d /tmp/cassandra && \
    rm -f cassandra_simple_auth.zip && \
    apk del dependencies && \
    cp /tmp/cassandra/lib/*.jar /usr/local/cassandra/lib/ && \
    cp /tmp/cassandra/conf/*.properties /usr/local/cassandra/conf/ && \
    rm -rf /tmp/cassandra && \
    echo "aoyagi=aoyagi_pwd" >> /usr/local/cassandra/conf/passwd.properties && \
    echo "\n #IMBox settings" >> /usr/local/cassandra/conf/access.properties && \
    echo "imbox_keyspace.<rw>=aoyagi" >> /usr/local/cassandra/conf/access.properties && \
    echo "imbox_keyspace.<ro>=user" >> /usr/local/cassandra/conf/access.properties && \
    echo "imbox_keyspace.*.<rw>=aoyagi" >> /usr/local/cassandra/conf/access.properties && \
    echo "imbox_keyspace.*.<ro>=user" >> /usr/local/cassandra/conf/access.properties && \
    chmod +x /usr/local/cassandra/entrypoint.sh

ENTRYPOINT ["/usr/local/cassandra/entrypoint.sh"]


# 7199: jmx port
# 9160: cassandra port
EXPOSE 7199 9160
