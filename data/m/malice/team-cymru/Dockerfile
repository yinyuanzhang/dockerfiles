FROM gliderlabs/alpine

MAINTAINER blacktop, https://github.com/blacktop

COPY . /go/src/github.com/maliceio/malice-team-cymru
RUN apk-install -t build-deps go git mercurial \
  && set -x \
  && echo "Building info Go binary..." \
  && cd /go/src/github.com/maliceio/malice-team-cymru \
  && export GOPATH=/go \
  && go version \
  && go get \
  && go build -ldflags "-X main.Version=$(cat VERSION) -X main.BuildTime=$(date -u +%Y%m%d)" -o /bin/team-cymru \
  && rm -rf /go \
  && apk del --purge build-deps

ENTRYPOINT ["/bin/team-cymru"]

CMD ["--help"]
