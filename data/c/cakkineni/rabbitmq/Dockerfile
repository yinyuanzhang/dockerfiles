FROM centos:centos7

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install wget logrotate rabbitmq-server; yum clean all


RUN /usr/lib/rabbitmq/bin/rabbitmq-plugins enable rabbitmq_management

ADD run-rabbitmq-server.sh /run-rabbitmq-server.sh
RUN chmod 750 ./run-rabbitmq-server.sh

# Define environment variables.
ENV RABBITMQ_LOG_BASE /data/log
ENV RABBITMQ_MNESIA_BASE /data/mnesia

# Define mount points.
VOLUME ["/data/log", "/data/mnesia"]

# 5672 rabbitmq-server - amqp port
# 15672 rabbitmq-server - for management plugin
EXPOSE 5672 15672

#ENV DEFAULT_VHOST_NAME develop

CMD ["/run-rabbitmq-server.sh"]
