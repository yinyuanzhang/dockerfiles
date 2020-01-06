FROM gcc:8 AS build
COPY noop.S .
RUN gcc -o noop -nostdlib -static -s -Wl,--build-id=none noop.S

FROM scratch
COPY --from=build noop /bin/chown
