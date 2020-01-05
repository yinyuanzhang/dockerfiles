FROM alpine:3.6

ADD dcraw.c /opt/dcraw/src/

RUN apk upgrade && \
    apk update && \
    apk add --no-cache musl-dev \
            gcc \
            libjpeg-turbo-dev \
            lcms2-dev \
            jasper-dev; \
    mkdir -p /opt/dcraw/bin; \
    gcc -o /opt/dcraw/bin/dcraw -O4 /opt/dcraw/src/dcraw.c -lm -ljasper -ljpeg -llcms2

ENV PATH="/opt/dcraw/bin:${PATH}"
ENTRYPOINT ["dcraw"]
