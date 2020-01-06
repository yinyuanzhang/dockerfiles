FROM ruby:2.4.2-alpine3.6

ENV \
GEMINABOX_VERSION=0.13.10

RUN \
apk add --no-cache curl ;\
gem install geminabox -v ${GEMINABOX_VERSION} ;\
mkdir -p /opt/geminabox/data

ADD /conf.d/* /opt/geminabox/conf/

EXPOSE 9292

ADD docker-*.sh /

HEALTHCHECK --interval=10s --timeout=10s --retries=90 CMD /docker-healthcheck.sh

WORKDIR /opt/geminabox/conf
ENTRYPOINT [ "/docker-entrypoint.sh" ]
CMD [ "rackup", "--host", "0.0.0.0" ]
