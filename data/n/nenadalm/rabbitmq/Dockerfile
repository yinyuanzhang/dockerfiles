FROM nenadalm/fedora

RUN yum upgrade -y
RUN yum install -y \
    librabbitmq-devel
RUN yum clean all

WORKDIR /tmp
RUN curl --output rabbitmq-server.rpm http://www.rabbitmq.com/releases/rabbitmq-server/v3.4.3/rabbitmq-server-3.4.3-1.noarch.rpm
RUN yum localinstall -y rabbitmq-server.rpm
RUN rm rabbitmq-server.rpm
RUN rabbitmq-plugins enable rabbitmq_management

COPY configuration /

EXPOSE 5672
EXPOSE 15672
CMD rabbitmq-server

