FROM docker.elastic.co/beats/filebeat:6.2.4

USER root

RUN yum -y update && \
    yum -y install wget nc

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

COPY filebeat.yml /usr/share/filebeat/filebeat.yml

RUN mkdir -p /usr/share/dockerlogs/data \
    && chown -R root /usr/share/filebeat/data \
    && chmod -R go-w /usr/share/filebeat/data

ENTRYPOINT ["filebeat"]
