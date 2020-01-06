FROM nawoschiknicholas/java_base

# Change to appuser
USER appuser

# Download. extract, and set folder permissions for Kafka
RUN wget --no-check-certificate -P /tmp https://www-us.apache.org/dist/kafka/2.2.0/kafka_2.12-2.2.0.tgz
RUN tar xvzf /tmp/kafka_2.12-2.2.0.tgz -C /opt
RUN rm /tmp/kafka_2.12-2.2.0.tgz

RUN mkdir /opt/kafka_2.12-2.2.0/logs
RUN chmod 777 /opt/kafka_2.12-2.2.0/config && \
        chmod 777 /opt/kafka_2.12-2.2.0/logs

# Copy script to run on container start-up
COPY --chown=appuser starterScript.sh /entrypoint
RUN chmod 777 /entrypoint/starterScript.sh

# Default Environment Variables
ENV ZOOKEEPER_HOST=zookeeper:2181
ENV BROKER_ID=0
ENV LISTENERS=PLAINTEXT://localhost:9092
ENV ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
ENV LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT

# Expose the port to use
EXPOSE 9092

# Run the starter script
ENTRYPOINT ["/entrypoint/starterScript.sh"]