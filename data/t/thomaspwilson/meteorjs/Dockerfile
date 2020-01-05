FROM ubuntu:wily

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        sudo \
 && curl https://install.meteor.com/ | sh \
 && rm -rf /var/lib/apt/lists/*

COPY rootfs/ /
RUN chmod 755 /sbin/entrypoint.sh

VOLUME ["/srv/meteor"]
EXPOSE 3000
ENTRYPOINT ["/sbin/entrypoint.sh"]
CMD ["meteor"]