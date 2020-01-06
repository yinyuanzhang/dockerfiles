FROM docker.elastic.co/kibana/kibana:7.5.0

MAINTAINER Justin Henderson justin@hasecuritysolutions.com

USER root
RUN cd /tmp \
    && yum install wget -y \
    && wget https://hasecuritysolutions.com/readonlyrest_kbn_enterprise-1.18.10_es7.5.0.zip -O /tmp/readonlyrest-plugin.zip \
    && chmod 777 /tmp/readonlyrest-plugin.zip \
    && chown kibana:kibana /tmp/readonlyrest-plugin.zip \
    && yum remove wget -y \
    && yum clean all -y
USER kibana
RUN cd /usr/share/kibana \
    && bin/kibana-plugin install -q file:///tmp/readonlyrest-plugin.zip \
    && rm -f /tmp/readonlyrest-plugin.zip \
    && bin/kibana-plugin install -q https://github.com/bitsensor/elastalert-kibana-plugin/releases/download/1.1.0/elastalert-kibana-plugin-1.1.0-7.5.0.zip

STOPSIGNAL SIGTERM
