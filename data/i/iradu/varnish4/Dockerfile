FROM debian:jessie
MAINTAINER "Ionut Radu" <iradu@iradu.ro>

COPY bin/docker-install.sh /tmp/docker-install.sh
RUN /tmp/docker-install.sh \
 && rm -rvf /tmp/*

COPY bin/*.py bin/track* bin/*.sh  /
COPY bin/reload                    /usr/bin/reload
COPY bin/default.vcl               /etc/varnish/default.vcl

EXPOSE 6081 6085

HEALTHCHECK --interval=1m --timeout=3s \
  CMD ["/docker-healthcheck.sh"]

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["varnish"]
