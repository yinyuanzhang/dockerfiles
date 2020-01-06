FROM frolvlad/alpine-glibc
MAINTAINER lida.he@dell.com

ENV METRICBEAT_VERSION=5.2.2

RUN apk add --no-cache \
      ca-certificates \
      curl

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/metricbeat/metricbeat-${METRICBEAT_VERSION}-linux-x86_64.tar.gz && \
    tar -xvvf metricbeat-${METRICBEAT_VERSION}-linux-x86_64.tar.gz && \
    mv metricbeat-${METRICBEAT_VERSION}-linux-x86_64/ /metricbeat && \
    mv /metricbeat/metricbeat.yml /metricbeat/metricbeat.example.yml && \
    chmod +x /metricbeat/metricbeat

WORKDIR /metricbeat

ADD entrypoint.sh /metricbeat/entrypoint.sh

ENTRYPOINT ["/metricbeat/entrypoint.sh"]
CMD ["/metricbeat/metricbeat", "-e", "-v", "-c", "/metricbeat/metricbeat-out.yml"]
