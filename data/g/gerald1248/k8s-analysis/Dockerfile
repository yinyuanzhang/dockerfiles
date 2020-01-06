FROM gliderlabs/alpine:latest
# skip as already installed: netstat, nslookup, telnet, traceroute, ping
# dig from bind-tools; ab from apache2-utils
RUN apk add --no-cache curl bind-tools apache2-utils mysql-client postgresql-client
RUN addgroup -S app && adduser -S -g app app
WORKDIR /app
USER app
CMD ["/bin/sh", "-c", "while true; do sleep 60; done"]
