FROM golang:1.11

COPY . /app
WORKDIR /app

RUN go mod download
RUN go build -o bin/api -v -ldflags '-s -w' cli/api/main.go && \
  go build -o bin/engine -v -ldflags '-s -w' cli/engine/main.go && \
  go build -o bin/launcher -v -ldflags '-s -w' cli/launcher/main.go && \
  go build -o bin/watcher -v -ldflags '-s -w' cli/watcher/main.go && \
  go build -o bin/websocket -v -ldflags '-s -w' cli/websocket/main.go && \
  go build -o bin/maker -v -ldflags '-s -w' cli/maker/main.go

FROM alpine
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2

RUN apk update && \
    apk add sqlite ca-certificates && \
    rm -rf /var/cache/apk/*

COPY --from=0 /app/db /db/
COPY --from=0 /app/bin/api /bin/
COPY --from=0 /app/bin/maker /bin/
COPY --from=0 /app/bin/engine /bin/
COPY --from=0 /app/bin/launcher /bin/
COPY --from=0 /app/bin/watcher /bin/
COPY --from=0 /app/bin/websocket /bin/