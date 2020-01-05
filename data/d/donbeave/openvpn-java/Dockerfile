FROM openjdk:11.0.2-jre-slim-stretch

MAINTAINER Alexey Zhokhov <alexey@zhokhov.com>

ENV DEBIAN_FRONTEND noninteractive

# Update apt-get
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
               openvpn \
    && rm -rf /var/lib/apt/lists/* \
              /tmp/*

COPY docker-entrypoint.sh /
RUN chmod a+x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/bin/sleep", "300"]
