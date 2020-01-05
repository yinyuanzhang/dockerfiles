FROM evlos/openjdk7

MAINTAINER Evlos <4tyle8@gmail.com>

RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor

RUN mkdir -p /app_config && \
	cd /app_config
ADD supervisord.conf /app_config/supervisord.conf

VOLUME ["/app"]
EXPOSE 60000
WORKDIR /app_config
CMD ["/usr/bin/supervisord"]
