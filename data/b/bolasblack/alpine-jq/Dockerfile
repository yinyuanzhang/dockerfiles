FROM alpine:latest

ENV JQ_VERSION 1.6

RUN apk update && apk --no-cache add jq

ENTRYPOINT ["jq"]
CMD ["-h"]
