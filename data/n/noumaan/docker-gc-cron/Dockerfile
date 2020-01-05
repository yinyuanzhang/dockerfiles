# Adds cron functionality on top of docker-gc
# From spotify/docker-gc/Dockerfile

FROM gliderlabs/alpine:3.2

ENV DOCKER_VERSION 1.11.2

# We get curl so that we can avoid a separate ADD to fetch the Docker binary, and then we'll remove it
RUN apk --update add bash curl \
  && cd /tmp/ \
  && curl -sSL -O https://get.docker.com/builds/Linux/x86_64/docker-${DOCKER_VERSION}.tgz \
  && tar zxf docker-${DOCKER_VERSION}.tgz \
  && mkdir -p /usr/local/bin/ \
  && mv ./docker/docker /usr/local/bin/ \
  && chmod +x /usr/local/bin/docker \
  && apk del curl \
  && rm -rf /tmp/* \
  && rm -rf /var/cache/apk/*

ADD https://raw.githubusercontent.com/spotify/docker-gc/master/docker-gc /docker-gc
COPY build/executed-by-cron.sh /executed-by-cron.sh
COPY build/generate-crontab.sh /generate-crontab.sh
COPY build/entrypoint.sh  /entrypoint.sh

RUN chmod +x /docker-gc /executed-by-cron.sh /generate-crontab.sh /entrypoint.sh

VOLUME /var/lib/docker-gc

CMD ["/entrypoint.sh"]
