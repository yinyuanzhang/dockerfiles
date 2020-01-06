FROM ubuntu:16.04

MAINTAINER Leo Unbekandt <leo@scalingo.com>
MAINTAINER David Young <davidy@funkypenguin.co.nz>

# BUILD_DATE and VCS_REF are immaterial, since this is a 2-stage build, but our build
# hook won't work unless we specify the args
ARG BUILD_DATE
ARG VCS_REF

# Good docker practice, plus we get microbadger badges
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.vcs-url="https://github.com/funkypenguin/docker-munin-server.git" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.schema-version="2.2-r1"

RUN adduser --system --home /var/lib/munin --shell /bin/false --uid 1103 --group munin

RUN apt-get update -qq && RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive \
    apt-get install -y -qq git cron munin munin-node nginx wget heirloom-mailx patch spawn-fcgi libcgi-fast-perl
RUN rm /etc/nginx/sites-enabled/default && mkdir -p /var/cache/munin/www && chown munin:munin /var/cache/munin/www && mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin
RUN git clone https://github.com/munin-monitoring/contrib.git /tmp/munstrap && \
   cp -rb /tmp/munstrap/templates/munstrap/templates /etc/munin && \ 
   cp -rb /tmp/munstrap/templates/munstrap/static /etc/munin && \
   rm -rf /var/www/munin/* && rm -rf /tmp/munstrap

VOLUME /var/lib/munin
VOLUME /var/log/munin

ADD ./munin.conf /etc/munin/munin.conf
ADD ./nginx.conf /etc/nginx/nginx.conf
ADD ./nginx-munin /etc/nginx/sites-enabled/munin
ADD ./start-munin.sh /munin
ADD ./munin-graph-logging.patch /usr/share/munin
ADD ./munin-update-logging.patch /usr/share/munin

RUN cd /usr/share/munin && patch munin-graph < munin-graph-logging.patch && patch munin-update < munin-update-logging.patch

EXPOSE 8080
CMD ["bash", "/munin"]
