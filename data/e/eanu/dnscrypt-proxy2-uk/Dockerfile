FROM alpine:edge
RUN apk update && apk --no-cache add ca-certificates dnscrypt-proxy
ADD config /config
EXPOSE 53/udp

CMD ["dnscrypt-proxy", "-config", "/config/dnscrypt-proxy.toml"]
