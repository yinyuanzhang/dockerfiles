FROM golang:1.10.3-alpine AS build

RUN apk add --update-cache \
  git

ENV rainy_cape_dir="/go/src/github.com/rainycape"

RUN mkdir -p ${rainy_cape_dir}

RUN git clone https://github.com/rainycape/governator.io.git ${rainy_cape_dir}/governator.io
RUN git clone https://github.com/rainycape/gondola.git ${rainy_cape_dir}/gondola
WORKDIR ${rainy_cape_dir}/gondola
RUN git checkout 0b3f3e3a8b1b8fdc0199ed33288cc1511b9212c9
RUN go get -u -v github.com/dchest/uniuri
RUN go get -u -v github.com/rainycape/unidecode
RUN go get -u -v github.com/rainycape/vfs
RUN go get -u -v golang.org/x/net/websocket
RUN go get -u -v gopkg.in/yaml.v1
RUN go get -u -v golang.org/x/crypto/pbkdf2
RUN go get -u -v github.com/rainycape/semver
RUN ln -s ${rainy_cape_dir}/gondola /go/src/gnd.la
WORKDIR ${rainy_cape_dir}/governator.io
RUN go build -tags netgo

FROM alpine:3.7
LABEL maintainer=godsboss@gmx.de
LABEL version=1.0.0
EXPOSE 37831
COPY --from=build /go/src/github.com/rainycape/governator.io/governator.io /governator.io
COPY --from=build /go/src/github.com/rainycape/governator.io/app.conf /app.conf
COPY --from=build /go/src/github.com/rainycape/governator.io/assets /assets
COPY --from=build /go/src/github.com/rainycape/governator.io/tmpl /tmpl
ENTRYPOINT /governator.io
