FROM openjdk:14-buster


# Directory to store kafka config
WORKDIR /opt/kafka_config

# Directory to store kafka jaas files
WORKDIR /opt/kafka_jaas

# Directory to store kafka logs
WORKDIR /opt/kafka-logs

WORKDIR /

# Download kafka
RUN wget http://mirrors.ukfast.co.uk/sites/ftp.apache.org/kafka/2.3.0/kafka_2.12-2.3.0.tgz

# Extract kafka
RUN tar -xzf kafka_2.12-2.3.0.tgz

WORKDIR kafka_2.12-2.3.0
