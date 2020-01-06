FROM alpine:latest

RUN set -x &&\
    apk update &&\
    apk add --no-cache jq &&\
    latest=$(wget -q https://api.github.com/repos/gohugoio/hugo/tags -O - |\
        jq  .[0]."name" | sed 's/"//g') &&\
    latestNoV="$(echo $latest | sed 's/v//g')" &&\
    wget -O - \
        "https://github.com/gohugoio/hugo/releases/download/${latest}/hugo_${latestNoV}_Linux-64bit.tar.gz" |\
        tar -xzf - hugo -C /usr/bin &&\
    apk del jq &&\
    rm -rf /var/cache/apk/*
ENTRYPOINT ["/usr/bin/hugo"]