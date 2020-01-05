FROM openjdk:11-slim-buster

LABEL maintainer="zoredache@gmail.com"

RUN apt-get update \
  && </dev/null DEBIAN_FRONTEND=noninteractive \
    apt-get --yes install --no-install-recommends \
      tmux procps vim-tiny \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /srv/project

RUN </dev/null adduser --quiet --disabled-password --gecos '' --uid 1000 mc

EXPOSE 25565/tcp
EXPOSE 25577/udp
EXPOSE 8804/tcp
WORKDIR /srv/project/
CMD ["/usr/bin/tmux", "new-session", "-s", "mc", "/bin/bash"]

USER 1000

