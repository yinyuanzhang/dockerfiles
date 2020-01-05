FROM debian:buster-slim AS build

ARG MIRROR=https://ftp.gnu.org/gnu/bash/

RUN apt-get update \
    && apt-get install -y curl build-essential bison flex

RUN mkdir /build \
    && cd /build \
    && curl -s "${MIRROR}" \
      | sed -n "s#.*bash-[2-9].*.tar.gz\">\([^<]*\).*#${MIRROR}/\1#p" \
      | xargs -rn 1 curl -O

#
# Attempt to build as many bash's as possible.
# Note: Does not abort if any of the compilations fail.
#
RUN cd /build \
    && ls bash-*.tar.gz | \
       xargs -I{} basename "{}" .tar.gz | \
       xargs -I{} -P 4 -r bash -c '( \
        tar zxf "{}.tar.gz" \
        && cd "{}" \
        && ./configure \
        && make -s \
        && cp "bash" "/usr/local/bin/{}" )' || true

FROM debian:buster-slim

COPY --from=build /usr/local/bin/* /usr/local/bin/
