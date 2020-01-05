ARG DOCKER_VER=latest
FROM docker:$DOCKER_VER

COPY sch_prune.sh /sch_prune.sh

# VOLUME /var/run/docker.sock /var/run/docker.sock

ENTRYPOINT [ "/sch_prune.sh" ]
