FROM golang:1.10.2 as builder

WORKDIR /go/src/github.com/keycloak/keycloak-gatekeeper
COPY . ./

RUN go get -u github.com/golang/dep/cmd/dep \
    && dep ensure \
    && go test

RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o bin/keycloak-gatekeeper .

FROM alpine:3.7
MAINTAINER Rohith Jayawardene <gambol99@gmail.com>
LABEL Name=keycloak-proxy \
      Release=https://github.com/gambol99/keycloak-proxy \
      Url=https://github.com/gambol99/keycloak-proxy \
      Help=https://github.com/gambol99/keycloak-proxy/issues

RUN apk add --no-cache ca-certificates

ADD templates/ /opt/templates

COPY --from=builder /go/src/github.com/keycloak/keycloak-gatekeeper/bin/keycloak-gatekeeper /opt/keycloak-gatekeeper

WORKDIR "/opt"

ENTRYPOINT ["/opt/keycloak-gatekeeper"]
