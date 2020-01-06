FROM ivanpondal/alpine-latex:1.1.0

 RUN apk update \
  && apk add ca-certificates wget \
  && wget -O /tmp/pandoc.tar.gz https://github.com/jgm/pandoc/releases/download/2.2.3.2/pandoc-2.2.3.2-linux.tar.gz \
  && tar xvzf /tmp/pandoc.tar.gz --strip-components 1 -C /usr/local/ \
  && update-ca-certificates \
  && apk del wget \
  && rm /tmp/pandoc.tar.gz

ARG PUID=1005
ARG PGID=1005

RUN addgroup -g ${PGID} pandoc \
 && adduser -D -u ${PUID} -G pandoc pandoc

USER pandoc
