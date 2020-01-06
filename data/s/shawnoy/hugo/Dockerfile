FROM golang:1.11-alpine3.9 AS build

WORKDIR /go/src

RUN apk add --no-cache git gcc g++ binutils

ARG HUGO_VERSION=v0.61.0
RUN git clone --single-branch --branch ${HUGO_VERSION} https://github.com/gohugoio/hugo.git

WORKDIR /go/src/hugo

ENV GO111MODULE=on
ENV CGO_ENABLED=0
ENV GOOS=linux

RUN go get -d .

ARG BUILD_TAGS="99notag"
RUN go install -ldflags '-w -extldflags "-static"' -tags ${BUILD_TAGS}

FROM scratch

COPY --from=build /go/bin/hugo /usr/local/bin/hugo
ARG  WORKDIR="/site"

WORKDIR ${WORKDIR}
VOLUME  ${WORKDIR}

EXPOSE  1313

ENTRYPOINT [ "hugo" ]
CMD [ "--help" ]
