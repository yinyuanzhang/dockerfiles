FROM alpine AS BUILD

ADD https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 /tmp/jq
RUN chmod +x /tmp/jq

FROM scratch
ENTRYPOINT ["/usr/bin/jq"]
COPY --from=BUILD /tmp/jq /usr/bin/
USER 1000
