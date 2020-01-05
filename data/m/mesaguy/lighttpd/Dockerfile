ARG ALPINE_VERSION=latest
ARG SOURCE_COMMIT
ARG VERSION=latest

FROM alpine:$ALPINE_VERSION

RUN apk add --update --no-cache lighttpd lighttpd-mod_auth sed && \
    # Run lighttpd on port 8080
    sed -iE 's/.*server.port.*= 81/server.port = 8080/g' /etc/lighttpd/lighttpd.conf && \
    # Send error logs to stderr
    sed -iE 's/^server.errorlog.*/server.errorlog = "\/dev\/stderr"/g' /etc/lighttpd/lighttpd.conf && \
    # Always include custom config
    sed -iE 's/include "mime-types.conf"/include "mime-types.conf"\ninclude "custom.conf"/g' /etc/lighttpd/lighttpd.conf && \
    touch /etc/lighttpd/custom.conf && \
    # Allow lighttpd to run unprivileged
    chown lighttpd /run && \
    # Remove sed
    apk del sed

USER lighttpd

EXPOSE 8080

CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]

LABEL org.label-schema.name="lighttpd service" \
      org.label-schema.description="Simple unprivileged lighttpd service built for many architectures" \
      org.label-schema.url="https://hub.docker.com/repository/docker/mesaguy/lighttpd/" \
      org.label-schema.vcs-ref=$SOURCE_COMMIT \
      org.label-schema.vcs-url="https://github.com/mesaguy/docker-lighttpd" \
      org.label-schema.vendor="Mesaguy" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"
