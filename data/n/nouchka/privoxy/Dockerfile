##FROM jess/privoxy
FROM debian:jessie
MAINTAINER Jean-Avit Promis "docker@katagena.com"

RUN apt-get update && \
	DEBIAN_FRONTEND=noninteractive apt-get -yq install privoxy && \
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /etc/privoxy/custom/
RUN echo "" >> /etc/privoxy/config
RUN echo "actionsfile custom/custom.action" >> /etc/privoxy/config
RUN echo "filterfile custom/custom.filter" >> /etc/privoxy/config

EXPOSE 8118
ENTRYPOINT [ "privoxy", "--no-daemon" ]
CMD [ "/etc/privoxy/config" ]
