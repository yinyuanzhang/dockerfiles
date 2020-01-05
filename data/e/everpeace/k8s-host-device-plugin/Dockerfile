FROM golang:1.10.1 as build
WORKDIR /go/src/k8s-host-device-plugin

RUN go get github.com/golang/dep/cmd/dep
COPY Gopkg.toml Gopkg.lock ./
RUN dep ensure -v -vendor-only

COPY . .
RUN export CGO_LDFLAGS_ALLOW='-Wl,--unresolved-symbols=ignore-in-object-files' && \
    go install -ldflags="-s -w" -v k8s-host-device-plugin

FROM debian:stretch-slim
COPY --from=build /go/bin/k8s-host-device-plugin /bin/k8s-host-device-plugin

CMD ["/bin/k8s-host-device-plugin"]
