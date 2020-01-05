FROM postgres:10.3

RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \
  && echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \
  && apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y vim.tiny wget sudo net-tools ca-certificates unzip apt-transport-https acl \
  && rm -rf /var/lib/apt/lists/*

ENV PG_APP_HOME="/etc/docker-postgresql"\
  PG_USER=postgres \
  PG_HOME=/var/lib/postgresql \
  PG_RUNDIR=/run/postgresql \
  PG_LOGDIR=/var/log/postgresql \
  PG_CERTDIR=/etc/postgresql/certs \
  PG_BINDIR=/usr/lib/postgresql/${PG_MAJOR}/bin

RUN localedef -i en_IE -c -f UTF-8 -A /usr/share/locale/locale.alias en_IE.UTF-8
ENV LANG en_IE.utf8
ENV LC_MONETARY=en_IE.utf8

COPY runtime/ ${PG_APP_HOME}/
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

VOLUME ["${PG_HOME}", "${PG_RUNDIR}"]
WORKDIR ${PG_HOME}
ENTRYPOINT ["/sbin/entrypoint.sh"]
