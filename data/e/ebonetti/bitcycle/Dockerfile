#Compile Bitcycle
FROM golang as compiler
ENV GO_DIR /usr/local/go
ENV GOPATH /go
ENV PROJECT github.com/ebonetti/bitcycle
ADD . $GOPATH/src/$PROJECT
RUN go get $PROJECT/...;

#Install Bitcycle and run as Brian, unprivileged user
FROM debian:buster-slim
RUN set -eux; \
	useradd -r -m brian; \
    apt-get update; \
    apt-get install -y --no-install-recommends ca-certificates; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/;
COPY --from=compiler /go/bin/bitcycle /usr/local/bin
WORKDIR /home/brian
USER brian
ENTRYPOINT ["bitcycle"]