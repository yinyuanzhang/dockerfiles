# Kafka and Zookeeper

FROM openjdk:8-jre

ENV MIRROR_URL http://mirrors.gigenet.com/apache
ENV SIGNATURES_URL http://www-us.apache.org/dist
ENV DEBIAN_FRONTEND noninteractive
ENV SCALA_VERSION 2.12
ENV KAFKA_VERSION 1.0.1
ENV INSTALLER_NAME kafka_"${SCALA_VERSION}"-"${KAFKA_VERSION}"
ENV KAFKA_HOME /opt/"${INSTALLER_NAME}"

# Install Zookeeper and supervisor
RUN apt update && \
    # apt install -y zookeeper wget supervisor dnsutils && \
    apt install -y zookeeper supervisor && \
    rm -rf /var/lib/apt/lists/* && \
    apt clean

# Download Kafka and signatures
RUN curl --silent --show-error "${MIRROR_URL}"/kafka/"$KAFKA_VERSION"/"${INSTALLER_NAME}".tgz -o /tmp/"${INSTALLER_NAME}".tgz && \
    curl --silent --show-error "${SIGNATURES_URL}"/kafka/"$KAFKA_VERSION"/"${INSTALLER_NAME}".tgz.asc -o /tmp/"${INSTALLER_NAME}".tgz.asc && \
    curl --silent --show-error "${SIGNATURES_URL}"/kafka/KEYS -o /tmp/KEYS

# Verify and extract
RUN gpg --import /tmp/KEYS && \
    gpg --verify /tmp/"${INSTALLER_NAME}".tgz.asc /tmp/"${INSTALLER_NAME}".tgz && \
    tar xfz /tmp/"${INSTALLER_NAME}".tgz -C /opt && \
    rm /tmp/"${INSTALLER_NAME}".tgz

ADD scripts/start-kafka.sh /usr/bin/start-kafka.sh

# Supervisor config
ADD supervisor/kafka.conf supervisor/zookeeper.conf /etc/supervisor/conf.d/

# 2181 is zookeeper, 9092 is kafka
EXPOSE 2181 9092

CMD ["supervisord", "-n"]
