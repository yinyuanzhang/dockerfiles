FROM alpine:3.8
RUN apk add --no-cache bash
COPY ./entrypoint.sh /
COPY ./lorem-ipsum /
ENTRYPOINT ["/entrypoint.sh"]
