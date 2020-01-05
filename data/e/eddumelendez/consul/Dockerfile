FROM ubuntu:latest

MAINTAINER Eddú Meléndez <eddu.melendez@gmail.com>

RUN apt-get install -y wget unzip

EXPOSE 8500

RUN set -x \
        && cd /opt \
        && wget -O consul.zip https://dl.bintray.com/mitchellh/consul/0.5.2_linux_amd64.zip \
        && unzip consul.zip \
        && mv consul /usr/local/bin/ \
        && rm consul.zip*

RUN set -x \
        && cd /opt \
        && wget -O consul-ui.zip https://dl.bintray.com/mitchellh/consul/0.5.2_web_ui.zip \
        && unzip consul-ui.zip \
        && mv dist consul-ui \
        && rm consul-ui.zip*

ENTRYPOINT ["consul", "agent", "-server", "-bootstrap-expect", "1", "-data-dir", "/tmp/consul", "-ui-dir", "/opt/consul-ui", "-client", "0.0.0.0"]
