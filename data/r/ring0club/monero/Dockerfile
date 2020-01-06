FROM alpine:3.10.1
RUN apk upgrade \
    --repository https://nl.alpinelinux.org/alpine/edge/main \
    --no-cache
RUN apk add boost-chrono=1.69.0-r5 \
            boost-regex=1.69.0-r5 \
            boost-thread=1.69.0-r5 \
            boost-filesystem=1.69.0-r5 \
            boost-serialization=1.69.0-r5 \
            boost-program_options=1.69.0-r5 \
            unbound-libs=1.9.2-r0 \
            readline=8.0.0-r0 \
    --repository https://nl.alpinelinux.org/alpine/edge/main \
    --no-cache
RUN apk add miniupnpc=2.1.20190625-r0 \
    --repository https://nl.alpinelinux.org/alpine/edge/community \
    --no-cache
RUN apk add monero=0.14.1.0-r0 \
    --repository https://nl.alpinelinux.org/alpine/edge/testing \
    --no-cache && \
    mkdir /var/lib/monero
ENTRYPOINT ["monerod"]
CMD ["--data-dir=/var/lib/monero"]
