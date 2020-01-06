# This uses the official Docker images as base,
# and adds the official docker-compose binary.
#
ARG DOCKER_TAG=git
ARG DOCKER_COMPOSE_TAG=1.24.0
FROM docker/compose:${DOCKER_COMPOSE_TAG} AS docker-compose
FROM docker:${DOCKER_TAG}

# Add glibc, like the upstream docker-compose build.
# See:
# https://github.com/docker/compose/blob/master/Dockerfile.run
# https://github.com/sgerrand/alpine-pkg-glibc
# https://github.com/sgerrand/alpine-pkg-glibc/releases
ARG GLIBC_RELEASE=2.29-r0
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub && \
    wget -q "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/${GLIBC_RELEASE}/glibc-${GLIBC_RELEASE}.apk" && \
    apk add --no-cache "glibc-${GLIBC_RELEASE}.apk" && \
    rm /etc/apk/keys/sgerrand.rsa.pub "glibc-${GLIBC_RELEASE}.apk"
# XXX: Why are these needed?
RUN ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \
    ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib && \
    # ln -s /usr/lib/libgcc_s.so.1 /usr/glibc-compat/lib && \
    true

COPY --from=docker-compose /usr/local/bin/docker-compose /usr/local/bin/docker-compose
