FROM golang:1.11 AS builder

ENV	CGO_ENABLED=0 \
	GO111MODULE=on

WORKDIR /go/src/github.com/drone-plugins/drone-downstream
COPY . .

RUN go build -v -a -o release/linux/amd64/drone-downstream

FROM plugins/base:multiarch

LABEL maintainer="Drone.IO Community <drone-dev@googlegroups.com>" \
  org.label-schema.name="Drone Downstream" \
  org.label-schema.vendor="Drone.IO Community" \
  org.label-schema.schema-version="1.0"

COPY --from=builder /go/src/github.com/drone-plugins/drone-downstream/release/linux/amd64/drone-downstream /bin/
ENTRYPOINT ["/bin/drone-downstream"]

