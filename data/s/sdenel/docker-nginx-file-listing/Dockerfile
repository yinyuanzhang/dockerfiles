FROM nginx:1.17-alpine as base

MAINTAINER Simon DENEL, simondenel1@gmail.com

# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
ARG TIME_ZONE

# Logs to stdout / stderr
RUN ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log

# found dependancies using ldd /usr/sbin/nginx
# Distroless is a hard fork from https://github.com/kyos0109/nginx-distroless, thanks to him!
RUN mkdir -p /opt/var/cache/nginx && \
    cp -a --parents /usr/lib/nginx /opt && \
    cp -a --parents /usr/share/nginx /opt && \
    cp -a --parents /var/log/nginx /opt && \
    cp -aL --parents /var/run /opt && \
    cp -a --parents /etc/nginx /opt && \
    cp -a --parents /etc/passwd /opt && \
    cp -a --parents /etc/group /opt && \
    cp -a --parents /usr/sbin/nginx /opt && \
    cp -a --parents /lib/ld-musl-x86_64.so.* /opt && \
    cp -a --parents /usr/lib/libpcre.so.* /opt && \
    cp -a --parents /lib/libssl.so.1.* /opt && \
    cp -a --parents /lib/libcrypto.so.1.* /opt && \
    cp -a --parents /lib/libz.so.* /opt && \
    cp -a --parents /lib/ld-musl-x86_64.so.* /opt && \
    cp /usr/share/zoneinfo/${TIME_ZONE:-ROC} /opt/etc/localtime

FROM gcr.io/distroless/base

COPY --from=base /opt /

COPY default.conf /etc/nginx/conf.d/
COPY mime.types /etc/nginx/mime.types
COPY mime.types /etc/nginx/mime.types.default

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
