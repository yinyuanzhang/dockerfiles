FROM debian:buster-slim
LABEL maintainer="Jean-Avit Promis docker@katagena.com"

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq --no-install-recommends install \
		monit=* \
		rsync=* \
		openssl=* \
		ca-certificates=* && \
	chmod 600 /etc/monit/monitrc && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 2812

CMD ["monit", "-Ic", "/etc/monit/monitrc"]

