FROM ubuntu:18.04
MAINTAINER Roamlog Lee <roamlog@gmail.com>

ENV ZENTAO_VER=11.1
ENV DEBIAN_FRONTEND noninteractive

ARG ZENTAO_URL=http://dl.cnezsoft.com/zentao/${ZENTAO_VER}/ZenTaoPMS.${ZENTAO_VER}.stable.zbox_64.tar.gz

COPY docker-entrypoint /usr/local/bin/docker-entrypoint

RUN apt-get update \
       && apt-get install -y wget php-ldap --no-install-recommends \
       && rm -r /var/lib/apt/lists/* \
       && wget ${ZENTAO_URL} -O zbox.tar.gz \
       && mv zbox.tar.gz /tmp \
       && chmod +x /usr/local/bin/docker-entrypoint

HEALTHCHECK --start-period=20s --interval=45s --timeout=3s CMD wget http://localhost/ -O /dev/null || exit 1

EXPOSE 9999 33306

ENTRYPOINT ["docker-entrypoint"]
