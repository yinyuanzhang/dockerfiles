FROM nats-streaming:0.11.0-linux

FROM alpine:3.8

COPY --from=0 /nats-streaming-server /

# Expose client and management ports
EXPOSE 4222 8222

# Run with default memory based store
ENTRYPOINT ["/nats-streaming-server"]
CMD ["-m", "8222"]
