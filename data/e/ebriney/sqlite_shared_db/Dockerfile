FROM debian:jessie

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq install sqlite3 && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY run_script.sh /run_script.sh
RUN chmod +x /run_script.sh
VOLUME /data
ENTRYPOINT ["/run_script.sh"]
