FROM euskadi31/gentoo-portage:latest

MAINTAINER Axel Etcheverry <axel@etcheverry.biz>

ENV CRON_FILE /opt/cron/cronfile

RUN emerge sys-process/vixie-cron

ADD entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

CMD ["cron", "-n"]
