FROM debian:stable-slim


# Add files.
ADD bin/rabbitmq-start /usr/local/bin/
ADD rabbitmq.conf /etc/rabbitmq/

ENV SSH_PASSWD "root:Docker!"

# Install RabbitMQ.
RUN \
  apt-get update && \
  apt-get install -y apt-utils gnupg wget apt-transport-https dnsutils 2ping libnet-ifconfig-wrapper-perl iputils-ping nmap &&\
  apt-get install -y --no-install-recommends openssh-server && \
  wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | apt-key add - && \  
  echo "deb https://dl.bintray.com/rabbitmq-erlang/debian stretch erlang" > /etc/apt/sources.list.d/rabbitmq.list && \
  echo "deb https://dl.bintray.com/rabbitmq/debian stretch main" >> /etc/apt/sources.list.d/rabbitmq.list && \
  apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y rabbitmq-server && \
  rm -rf /var/lib/apt/lists/* && \
  rabbitmq-plugins enable rabbitmq_management rabbitmq_mqtt rabbitmq_peer_discovery_etcd rabbitmq_recent_history_exchange rabbitmq_sharding rabbitmq_shovel rabbitmq_shovel_management rabbitmq_stomp rabbitmq_tracing rabbitmq_web_dispatch rabbitmq_web_mqtt rabbitmq_web_stomp && \  
  chmod +x /usr/local/bin/rabbitmq-start && \
  echo "$SSH_PASSWD" | chpasswd 

ADD sshd_config /etc/ssh/


# Define environment variables.
#ENV RABBITMQ_LOG_BASE /data/log
ENV RABBITMQ_LOGS=-
ENV RABBITMQ_MNESIA_BASE /data/mnesia

# Define cluster discovery
ENV ETCD_HOST=localhost
ENV ETCD_PORT=2379
ENV RABBITMQ_USE_LONGNAME=true
ENV AUTOCLUSTER_TYPE=etcd
ENV AUTOCLUSTER_LOG_LEVEL=debug


# Define mount points.tee
VOLUME ["/data/log", "/data/mnesia"]

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["rabbitmq-start"]

# Expose ports.
EXPOSE 2222
EXPOSE 4369
EXPOSE 5671
EXPOSE 5672
EXPOSE 15672
EXPOSE 25672
