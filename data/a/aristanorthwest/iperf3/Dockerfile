FROM alpine:3.9 as iperf3

RUN \
    apk update && \
    apk add --no-cache iperf3

FROM alpine:3.9

# Expose the default iperf3 server port
EXPOSE 5201

COPY --from=iperf3 /usr/lib/libiperf.so.0 /usr/lib/libiperf.so.0
COPY --from=iperf3 /usr/bin/iperf3 /usr/bin/iperf3

# ENTRYPOINT ["/bin/ash", "-c", "while :; do sleep 2073600; done"]
ENTRYPOINT ["iperf3"]
