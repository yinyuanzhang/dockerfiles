FROM openjdk:8-alpine
MAINTAINER Jesper Jeeninga <jesper.jeeninga@trimm.nl>
ENV GALEN_VERSION=2.3.6
ENV TERM=ansi

RUN apk update && \
	apk upgrade && \
	apk add bash wget unzip --no-cache && \
	cd /tmp && \
	wget --no-verbose https://github.com/galenframework/galen/releases/download/galen-${GALEN_VERSION}/galen-bin-${GALEN_VERSION}.zip && \
	unzip galen-bin-${GALEN_VERSION}.zip && \ 
	rm galen-bin-${GALEN_VERSION}.zip && \
	cd galen-bin-${GALEN_VERSION} && \
	./install.sh && \
	cd /tmp && \
	rm -rf galen-bin-${GALEN_VERSION}/ && \
	rm -rf /var/cache/apk/* && \ 
	adduser -g "Galen user" -s /bin/bash -D galen
USER galen
WORKDIR /home/galen
ENTRYPOINT ["/bin/bash", "-c"]
