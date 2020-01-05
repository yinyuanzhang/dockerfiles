FROM ubuntu:14.04
EXPOSE 8888

RUN apt-get update \
 	&& apt-get install -y wget \
	&& echo "deb http://ubuntu.kurento.org trusty kms6" | sudo tee /etc/apt/sources.list.d/kurento.list \
	&& wget -O - http://ubuntu.kurento.org/kurento.gpg.key | apt-key add - \
	&& apt-get update \
	&& apt-get install -y kurento-media-server-6.0

ENTRYPOINT ["/usr/bin/kurento-media-server"]
