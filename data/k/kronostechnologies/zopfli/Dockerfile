FROM alpine as ssl
RUN apk add --update --no-cache ca-certificates

FROM gcc:6 AS builder

ADD . /code/
WORKDIR /code

RUN gcc src/zopfli/*.c -O2 -W -Wall -Wextra -Wno-unused-function -ansi -pedantic -lm -o zopfli
#RUN rm src/zopfli/zopfli_bin.c
#RUN g++ src/zopfli/*.c src/zopflipng/*.cc src/zopflipng/lodepng/*.cpp -O2 -W -Wall -Wextra -Wno-unused-function -ansi -pedantic -o zopflipng

FROM busybox:glibc

COPY --from=builder ["/code/zopfli", "/bin/"]
COPY --from=ssl /etc/ssl/certs /etc/ssl/certs
RUN mkdir -p /usr/bin && ln -s /bin/sh /usr/bin/sh
