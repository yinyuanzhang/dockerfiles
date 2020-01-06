FROM python:2.7-alpine
LABEL maintainer bitrox <proxy@bitrox.io>
LABEL maintainer funkypenguin <davidy@funkypenguin.co.nz>

# Now we DO need these, for the auto-labeling of the image
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/docker-mqtt-certbot-dns-alpine.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

# Set environment variables.
ENV TERM=xterm-color
ENV SHELL=/bin/bash

RUN \
	mkdir /cloudflare && \
	mkdir /mosquitto && \
	mkdir /mosquitto/log && \
	mkdir /mosquitto/conf && \
	apk update && \
	apk upgrade && \
	apk add \
		jq \
		curl \
		bash \
		coreutils \
                bind-tools \
        	py-crypto \
		ca-certificates \
        	certbot \
		mosquitto \
		mosquitto-clients && \
	rm -f /var/cache/apk/* && \
	pip install --upgrade pip && \
	pip install pyRFC3339 configobj ConfigArgParse &&\
        chown mosquitto /mosquitto/log

COPY run.sh /run.sh
COPY certbot.sh /certbot.sh
COPY cloudflare/* /cloudflare/
COPY restart.sh /restart.sh
COPY croncert.sh /etc/periodic/weekly/croncert.sh

RUN \
	chmod +x /run.sh && \
	chmod +x /certbot.sh && \
	chmod +x /restart.sh && \
	chmod +x /cloudflare/*.sh && \
	chmod +x /etc/periodic/weekly/croncert.sh

EXPOSE 1883
EXPOSE 8883

# This will run any scripts found in /scripts/*.sh
# then start mosquitto
CMD ["/bin/bash","-c","/run.sh"]
