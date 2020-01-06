FROM alpine:latest

MAINTAINER Lomig & Tux <lomigandtux@gmail.com>

ENV HUGO_VERSION 0.58.3
ENV HUGO_SOURCE hugo_${HUGO_VERSION}_Linux-64bit

RUN apk update && apk add py-pygments && rm -rf /var/cache/apk/*

ADD https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_SOURCE}.tar.gz /usr/local
RUN tar xzf /usr/local/${HUGO_SOURCE}.tar.gz -C /usr/local/bin \
        && rm /usr/local/${HUGO_SOURCE}.tar.gz \
        && rm /usr/local/bin/README.md \
        && rm /usr/local/bin/LICENSE

VOLUME /src
VOLUME /output

WORKDIR /src

EXPOSE 1313
ENTRYPOINT [ "hugo" ]
CMD [ "hugo" ]
