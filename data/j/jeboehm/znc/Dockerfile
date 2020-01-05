FROM alpine:3.4
MAINTAINER Jeffrey Boehm "jeff@ressourcenkonflikt.de"

ENV DATADIR="/znc-data"

RUN apk add --no-cache ca-certificates znc && \
    adduser zncrun -u 2000 -D -H && \
    mkdir $DATADIR && \
    chown zncrun $DATADIR

COPY rootfs/ /

VOLUME $DATADIR
USER zncrun

EXPOSE 6667 8080
ENTRYPOINT ["/entrypoint.sh"]
