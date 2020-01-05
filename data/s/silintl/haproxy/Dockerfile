FROM haproxy:1.4
MAINTAINER "Peter Kohler" <peter_kohler@sil.org>

RUN apt-get update && apt-get install -y \
  netcat \
  rsyslog \
  s3cmd

COPY expand.sh /
COPY start-services.sh /

ENTRYPOINT ["/expand.sh","/start-services.sh"]
CMD ["haproxy","-f","/etc/haproxy.cfg"]
