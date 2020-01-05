FROM dockerfile/java:oracle-java7
MAINTAINER Olaf Stauffer <olaf.stauffer@web.de>

ENV KIBANA_VERSION 4.0.0-beta3

RUN mkdir -p /opt &&\
	curl -SL https://download.elasticsearch.org/kibana/kibana/kibana-$KIBANA_VERSION.tar.gz |\
	tar -xzC /opt &&\
	mv /opt/kibana-$KIBANA_VERSION/config/kibana.yml /opt/kibana-$KIBANA_VERSION/config/kibana.yml.orig

EXPOSE 5601

RUN wget -P /opt https://github.com/olafstauffer/docker-starter/releases/download/v0.2.1/docker-starter_0.2.1_linux_386.tar.gz &&\
    cd /opt &&\
	tar xvzf docker-starter_0.2.1_linux_386.tar.gz &&\
	ln -s /opt/docker-starter_0.2.1_linux_386/docker-starter /usr/local/bin/ &&\
	rm docker-starter_0.2.1_linux_386.tar.gz

COPY kibana.yml.tmpl /opt/kibana-$KIBANA_VERSION/config/

CMD ["docker-starter", "-cmd", "/opt/kibana-{{E .KIBANA_VERSION}}/bin/kibana", "-dir", "/opt/kibana-{{E .KIBANA_VERSION}}/config"]
