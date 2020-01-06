FROM alpine
LABEL "MAINTAINER" "Manuel Manhart <manuel@manhart.space>"
ENV CONFIG_PATH=/etc/selfhost
ENV LOG=/var/log/container.log
ENV DEVICE=router
ENV TOOL=wget
ENV URL="remote.selfhost.de/ remote.ns4you.de/"

# Add crontab file in the cron directory
ADD content/scripts/ /scripts/
ADD IMAGE_NAME /
ADD IMAGE_VERSION /
COPY content/crontab /var/spool/cron/crontabs/root
RUN chmod +x /scripts/*.sh && \
    apk add --update openssl ca-certificates && \
	rm -rf /var/cache/apk/*
ENTRYPOINT ["/scripts/start.sh"]

HEALTHCHECK --interval=30s --timeout=3s \
  CMD /scripts/healthcheck.sh || exit 1