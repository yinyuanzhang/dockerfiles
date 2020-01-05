FROM circleci/golang:1.11

MAINTAINER kaiserkarel
LABEL description="a Go image for CI purposes"
LABEL supported="CircleCI"
LABEL version="0.0.2"

ENV GORELEASER_VERSION=0.79.0
ENV GORELEASER_SHA=14d24fdfdc8a7aff0956e4c0dcfad8a71fbaed804013be4ee93d26955dc75704

ENV GORELEASER_DOWNLOAD_FILE=goreleaser_Linux_x86_64.tar.gz
ENV GORELEASER_DOWNLOAD_URL=https://github.com/goreleaser/goreleaser/releases/download/v${GORELEASER_VERSION}/${GORELEASER_DOWNLOAD_FILE}

RUN  wget ${GORELEASER_DOWNLOAD_URL}; \
			echo "$GORELEASER_SHA $GORELEASER_DOWNLOAD_FILE" | sha256sum -c - || exit 1; \
			tar -xzf $GORELEASER_DOWNLOAD_FILE -C /usr/bin/ goreleaser; \
			rm $GORELEASER_DOWNLOAD_FILE;

RUN sudo chown circleci:circleci -R /go
RUN sudo chown circleci:circleci -R /usr/local/bin

RUN curl -sfL https://install.goreleaser.com/github.com/golangci/golangci-lint.sh | bash -s -- -b $GOPATH/bin v1.12.3

ENV GO111MODULE="on"
RUN GO111MODULE=off go get github.com/dave/courtney
RUN GO111MODULE=off go get github.com/mattn/goveralls
RUN GO111MODULE=off go get github.com/golang/mock/gomock
RUN GO111MODULE=off go install github.com/golang/mock/gomock

USER circleci

CMD ["/bin/sh"]
