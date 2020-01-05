FROM alpine

RUN apk add -U iperf && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["iperf"]
