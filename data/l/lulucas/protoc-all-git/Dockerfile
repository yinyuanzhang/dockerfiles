FROM lulucas/protoc-gen-validate AS validate
FROM namely/protoc-all

COPY --from=validate /go/bin/protoc-gen-validate /usr/local/bin/
COPY entrypoint.sh /usr/local/bin
RUN chmod +x /usr/local/bin/entrypoint.sh

RUN apk update && apk add --no-cache git
