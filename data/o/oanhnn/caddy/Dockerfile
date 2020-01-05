#
# Build stage
#
FROM golang:alpine as build

# args
ARG caddy_version="0.11.2"
ARG caddy_plugins="git,cors,realip,expires,cache"
ARG caddy_telemetry="true"
ARG upx_version="3.95"

# deps
RUN apk add --no-cache git xz curl ca-certificates

# scripts
COPY scripts/* /usr/bin/

# build
RUN VERSION=$caddy_version PLUGINS=$caddy_plugins ENABLE_TELEMETRY=$caddy_telemetry \
    /usr/bin/build.sh /usr/bin/caddy

# compress
RUN VERSION=$upx_version \
    /usr/bin/compress.sh /usr/bin/caddy

# process wrapper
RUN go get -v github.com/abiosoft/parent \
 && cp $GOPATH/bin/parent /usr/bin/parent

# test
RUN /usr/bin/caddy -version \
 && /usr/bin/caddy -plugins

#
# Final image
#
FROM scratch

# set default caddypath
ENV CADDYPATH=/etc/.caddy

# copy binary and ca certs
COPY --from=build /usr/bin/parent /bin/parent
COPY --from=build /usr/bin/caddy  /bin/caddy
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

# copy default caddyfile
COPY Caddyfile /etc/Caddyfile

# serve from /app
WORKDIR /app
COPY index.html /app/index.html

EXPOSE 80 443 2015
CMD ["/bin/parent", "/bin/caddy", "--conf=/etc/Caddyfile", "--log=stdout", "--agree=true"]
