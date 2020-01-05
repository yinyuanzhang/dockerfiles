FROM alpine:3.9

ENV HOST_DOMAIN host.docker.internal
ENV ENTRYPOINT_DIR /alpine-base-entrypoint.d

COPY scripts/configure_docker_host_hostname.sh /alpine-base-entrypoint.d/

RUN set -xe && \
    apk add --update --no-cache --progress tzdata && \
    chmod -R +x $ENTRYPOINT_DIR/ /etc/profile.d/ && \
    run-parts --exit-on-error $ENTRYPOINT_DIR/

ENV TZ America/Denver