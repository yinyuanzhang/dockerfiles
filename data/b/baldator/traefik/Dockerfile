FROM i386/alpine:3.9

ENV TRAEFIK_VERSION v2.0.5

RUN apk --no-cache add ca-certificates tzdata
RUN set -ex; \
        apkArch="$(apk --print-arch)"; \
        case "$apkArch" in \
                armhf) arch='armv6' ;; \
                aarch64) arch='arm64' ;; \
                x86_64) arch='amd64' ;; \
                x86) arch='386' ;; \
                *) echo >&2 "error: unsupported architecture: $apkArch"; exit 1 ;; \
        esac; \
        wget --quiet -O /tmp/traefik.tar.gz "https://github.com/containous/traefik/releases/download/$TRAEFIK_VERSION/traefik_${TRAEFIK_VERSION}_linux_$arch.tar.gz"; \
        tar xzvf /tmp/traefik.tar.gz -C /usr/local/bin traefik; \
        rm -f /tmp/traefik.tar.gz; \
        chmod +x /usr/local/bin/traefik
COPY entrypoint.sh /
RUN ln -s /var/run/balena.sock /var/run/docker.sock
EXPOSE 80
RUN adduser -D -u 1000 appuser
USER appuser

ENTRYPOINT ["sh", "/entrypoint.sh"]
CMD ["traefik"]

# Metadata
LABEL org.opencontainers.image.vendor="Containous" \
      org.opencontainers.image.url="https://traefik.io" \
      org.opencontainers.image.title="Traefik" \
      org.opencontainers.image.description="A modern reverse-proxy" \
      org.opencontainers.image.version="v2.0.0-alpha4" \
      org.opencontainers.image.documentation="https://docs.traefik.io"
