FROM golang

HEALTHCHECK --interval=60s --timeout=2s --retries=12 \
  CMD curl --silent --fail localhost/health || exit 1

WORKDIR /go/src/bitbucket.org/sismedico/backend

ADD . .

RUN go get -d -v ./...
RUN go install -v ./...

EXPOSE 80

ENTRYPOINT /go/bin/backend
