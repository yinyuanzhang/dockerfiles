FROM openjdk:8-jdk-alpine

ENV OPENHAB_VERSION 1.8.3

RUN apk add --no-cache wget && \
	wget --quiet --no-cookies -O /tmp/distribution-runtime.zip https://bintray.com/artifact/download/openhab/bin/distribution-$OPENHAB_VERSION-runtime.zip && \
	mkdir -p /opt/openhab/logs && \
	unzip -q -d /opt/openhab /tmp/distribution-runtime.zip && \
	chmod +x /opt/openhab/start.sh && \
	mv /opt/openhab/configurations /etc/openhab && \
	ln -s /etc/openhab /opt/openhab/configurations

EXPOSE 8080 8443 5555

CMD ["/opt/openhab/start.sh"]
