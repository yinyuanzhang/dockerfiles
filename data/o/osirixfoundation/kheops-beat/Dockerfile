FROM alpine:3.6

WORKDIR /install

ENV FILEBEAT_VERSION 7.1.1
ENV METRICBEAT_VERSION 7.1.1

RUN apk add --no-cache curl


RUN mkdir deb

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-${METRICBEAT_VERSION}-amd64.deb
RUN mv metricbeat-${METRICBEAT_VERSION}-amd64.deb deb/metricbeat-amd64.deb

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-amd64.deb
RUN mv filebeat-${FILEBEAT_VERSION}-amd64.deb deb/filebeat-amd64.deb


RUN mkdir rpm

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-${METRICBEAT_VERSION}-x86_64.rpm
RUN mv metricbeat-${METRICBEAT_VERSION}-x86_64.rpm rpm/metricbeat-x86_64.rpm

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-x86_64.rpm
RUN mv filebeat-${FILEBEAT_VERSION}-x86_64.rpm rpm/filebeat-x86_64.rpm
