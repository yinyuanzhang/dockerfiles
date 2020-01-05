FROM ubuntu

RUN apt update
RUN apt install -y gnupg2 wget
RUN apt-key adv --keyserver "hkps.pool.sks-keyservers.net" --recv-keys "0x6B73A36E6026DFCA"
RUN wget -O - "https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc" | apt-key add -
RUN apt install -y apt-transport-https
RUN echo "# Source repository definition example \
# See below for supported distribution and component values \
# This repository provides Erlang packages \
deb https://dl.bintray.com/rabbitmq-erlang/debian $distribution erlang \
# This repository provides RabbitMQ packages \
deb https://dl.bintray.com/rabbitmq/debian $distribution main " > /etc/apt/sources.list.d/bintray.rabbitmq.list
RUN echo "deb https://dl.bintray.com/rabbitmq/debian bionic main" | tee /etc/apt/sources.list.d/bintray.rabbitmq.list
RUN apt install -y rabbitmq-server
COPY enabled_plugins /etc/rabbitmq/enabled_plugins 
COPY rabbitmq.config /etc/rabbitmq/rabbitmq.config

ENTRYPOINT ["rabbitmq-server"]
