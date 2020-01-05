FROM golang:alpine as base_builder

RUN apk add --no-cache git gcc musl-dev

COPY --from=abiosoft/caddy:builder /usr/bin/builder.sh /usr/bin/builder.sh

CMD ["/bin/sh", "/usr/bin/builder.sh"]


FROM base_builder as builder

ARG version="0.11.2"
ARG plugins="cache,cors,expires,ipfilter,prometheus,ratelimit,realip"
ARG enable_telemetry="false"

# process wrapper
RUN go get -v github.com/abiosoft/parent

RUN VERSION=${version} PLUGINS=${plugins} ENABLE_TELEMETRY=$enable_telemetry /bin/sh /usr/bin/builder.sh

# Reduce size of caddy and parent
RUN strip /install/caddy && strip /go/bin/parent 

# Check caddy version
RUN /install/caddy -version

# Print caddy plugins
RUN /install/caddy -plugins


FROM alpine:3.8

# Add certificates
RUN apk add --no-cache ca-certificates curl

ARG version="0.11.2"
LABEL caddy_version="true"

ENV ENABLE_TELEMETRY="false"

# Let's Encrypt Agreement
ENV ACME_AGREE="false"


EXPOSE 2015 9180 
VOLUME /srv

# install caddy
COPY --from=builder /install/caddy /usr/bin/caddy

# install process wrapper
COPY --from=builder /go/bin/parent /bin/parent


COPY --from=abiosoft/caddy /etc/Caddyfile /etc/Caddyfile
COPY --from=abiosoft/caddy /srv/index.html /srv/index.html


ENTRYPOINT ["/bin/parent", "caddy"]
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout", "--agree=$ACME_AGREE"]
