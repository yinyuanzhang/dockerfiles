FROM gocd/gocd-agent-alpine-3.5:v17.7.0

MAINTAINER durmaze

RUN \
  # install curl to download the Docker binaries
  apk add --no-cache curl && \
  curl -fsSLO https://get.docker.com/builds/Linux/x86_64/docker-latest.tgz && \
  tar --strip-components=1 -xvzf docker-latest.tgz -C /usr/local/bin && \
  rm -rf docker docker-latest.tgz && \
  # add goagent user "go" to docker group so that it can access docker.sock
  # "ping" group's GID collides with host's "docker" group's GID. simply remove group "ping"
  delgroup ping && \
  addgroup -g 999 docker && \
  addgroup go docker
