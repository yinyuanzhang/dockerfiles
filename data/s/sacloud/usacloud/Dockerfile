FROM alpine:3.10
MAINTAINER Kazumichi Yamamoto <yamamoto.febc@gmail.com>
LABEL MAINTAINER 'Kazumichi Yamamoto <yamamoto.febc@gmail.com>'

RUN set -x && apk add --no-cache --update zip ca-certificates

ADD https://github.com/sacloud/usacloud/releases/download/v0.31.1/usacloud_linux-amd64.zip ./
RUN unzip usacloud_linux-amd64.zip -d /bin; rm -f usacloud_linux-amd64.zip

VOLUME ["/workdir"]
WORKDIR /workdir

ENTRYPOINT ["/bin/usacloud"]
CMD ["--help"]
