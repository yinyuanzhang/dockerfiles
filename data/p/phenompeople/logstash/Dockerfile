#Base image
FROM phenompeople/oraclejdk:latest
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com" \
	  version="6.5.0" \
	  project="logstash"
ARG LOGSTASH_VERSION=6.5.0
ENV container docker \
    LOGSTASH_VERSION=${LOGSTASH_VERSION}
EXPOSE 5004
ARG APP_HOME=/usr/local/logstash
RUN groupadd -g 406 logstash && \
	useradd -u 406 -g 406 logstash && \
	wget -q -O /tmp/logstash.tar.gz https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.tar.gz && \
	tar -xzf /tmp/logstash.tar.gz -C /usr/local && \
	ln -sf /usr/local/logstash-${LOGSTASH_VERSION} ${APP_HOME}
RUN /usr/local/logstash/bin/logstash-plugin install logstash-input-jmx
ENTRYPOINT ["/usr/local/logstash/bin/logstash", "--path.config", "/etc/logstash/conf.d"]
