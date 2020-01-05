# Builder
FROM golang:1.12-alpine as builder

ENV VERSION=${VERSION:-"0.11.5"}

RUN apk add git sed

RUN git clone -b v${VERSION} https://github.com/mholt/caddy /go/src/github.com/mholt/caddy

WORKDIR /go/src/github.com/mholt/caddy/caddy/caddymain
RUN sed -i 's@var EnableTelemetry = true@var EnableTelemetry = false@g' run.go

# Plugins - cache,cors,expires,filebrowser,git,prometheus,ratelimit,realip
ENV after='// This is where other plugins get plugged in (imported)'
RUN sed -i "\@${after}@a _ \"github.com/nicolasazrak/caddy-cache\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/captncraig/cors\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/epicagency/caddy-expires\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/filebrowser/caddy\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/abiosoft/caddy-git\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/miekg/caddy-prometheus\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/xuqingfeng/caddy-rate-limit\"" run.go
RUN sed -i "\@${after}@a _ \"github.com/captncraig/caddy-realip\"" run.go

RUN go fmt run.go
RUN go get -d -v github.com/mholt/caddy/...
RUN go get -d -v github.com/caddyserver/builds

WORKDIR /go/src/github.com/mholt/caddy/caddy
RUN GOOS=linux GOARCH=amd64 go run build.go -goos=$GOOS -goarch=$GOARCH -goarm=$GOARM \
    && mkdir /install \
    && mv caddy /install

# Final image
FROM alpine:3.9

RUN apk add --no-cache openssh-client git

COPY --from=builder /install/caddy /usr/bin/caddy

RUN /usr/bin/caddy -version
RUN /usr/bin/caddy -plugins

EXPOSE 80 443 2015
VOLUME /root/.caddy /srv
WORKDIR /srv

COPY Caddyfile /etc/Caddyfile
COPY index.html /srv/index.html

ENTRYPOINT ["/usr/bin/caddy"]
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout", "-agree=false"]
