FROM nawoschiknicholas/java_base

# Change to appuser
USER appuser

# Download and extract the Zookeeper program to the specified path
RUN wget --no-check-certificate -P /tmp https://www-us.apache.org/dist/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz
RUN tar xvzf /tmp/zookeeper-3.4.14.tar.gz -C /opt
RUN rm /tmp/zookeeper-3.4.14.tar.gz

# Create Zookeeper configuration file
RUN echo tickTime=2000 > /opt/zookeeper-3.4.14/conf/zoo.cfg
RUN echo dataDir=/var/lib/zookeeper >> /opt/zookeeper-3.4.14/conf/zoo.cfg
RUN echo clientPort=2181 >> /opt/zookeeper-3.4.14/conf/zoo.cfg

# Expose the port to use
EXPOSE 2181

# Set the command to use on start
ENTRYPOINT ["/opt/zookeeper-3.4.14/bin/zkServer.sh", "start-foreground"]