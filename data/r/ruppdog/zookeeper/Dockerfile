FROM ruppdog/base:0.0.1

# Install Java
RUN apk --update add openjdk8-jre

# Install Zookeeper
ENV ZOOKEEPER_VERSION 3.4.8
RUN \
    wget http://mirrors.ibiblio.org/apache/zookeeper/zookeeper-$ZOOKEEPER_VERSION/zookeeper-$ZOOKEEPER_VERSION.tar.gz && \
    tar -C /app -xzvf zookeeper-$ZOOKEEPER_VERSION.tar.gz && \
    rm zookeeper-$ZOOKEEPER_VERSION.tar.gz

# Copy templates
COPY templates /app/templates

# Set up entrypoint
ADD entrypoint.sh /sbin/entrypoint.sh
ENTRYPOINT ["/sbin/entrypoint.sh"]

# Set working directory
WORKDIR /app/zookeeper-$ZOOKEEPER_VERSION/

# Run command
CMD [ "bin/zkServer.sh", "start-foreground" ]
