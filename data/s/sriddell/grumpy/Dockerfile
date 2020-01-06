# build stage
FROM golang:1.12-stretch AS build-env
RUN go version
RUN mkdir -p /app
COPY  . /app
RUN useradd -u 10001 webhook
RUN cd /app && CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"' -o grumpywebhook

FROM scratch
COPY --from=build-env /app/grumpywebhook .
COPY --from=build-env /etc/passwd /etc/passwd
USER webhook
ENTRYPOINT ["/grumpywebhook"]