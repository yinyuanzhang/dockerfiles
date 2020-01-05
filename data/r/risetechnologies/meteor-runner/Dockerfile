FROM node:8.11.4

MAINTAINER risetechnologies

ENV PATH=/opt/nodejs/bin:$PATH

RUN apt-get update \
  && apt-get install -y imagemagick \
  && apt-get autoremove -y \
  && rm -rf \
    /usr/share/doc /usr/share/doc-base /usr/share/man \
    /usr/share/locale /usr/share/zoneinfo \
    /var/lib/cache /var/lib/log /tmp/*

COPY install_dependencies.sh /opt/
COPY run_app.sh /opt/

CMD ["/opt/run_app.sh"]
