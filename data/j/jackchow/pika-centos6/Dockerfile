FROM centos:6

MAINTAINER jackchow "jack_chow621@sina.com"

RUN yum -y update && \
    yum  -y install wget && \
    wget https://github.com/Qihoo360/pika/archive/v2.3.6.tar.gz && \
    mv v2.3.6.tar.gz /opt && \
    tar -zxf /opt/v2.3.6.tar.gz && \
    rm -r /opt/v2.3.6.tar.gz

ENV PIKA  /opt/pika-v2.3.6
ENV PATH ${PIKA}/bin:${PATH}

ENV TZ Asia/Shanghai

WORKDIR ${PIKA}


EXPOSE 9221
