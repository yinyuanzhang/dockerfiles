FROM rabbitmq:management
LABEL description="RabbitMQ Autocluster" \
      maintainer="Djerfy <djerfy@gmail.com>"

ENV PLUGIN_VERSION=0.10.0

RUN apt-get update && \
    apt-get install -y wget

RUN cd /opt/rabbitmq/plugins && \
    wget -q https://github.com/rabbitmq/rabbitmq-autocluster/releases/download/${PLUGIN_VERSION}/autocluster-${PLUGIN_VERSION}.ez && \
    wget -q https://github.com/rabbitmq/rabbitmq-autocluster/releases/download/${PLUGIN_VERSION}/rabbitmq_aws-${PLUGIN_VERSION}.ez

RUN rabbitmq-plugins enable autocluster
