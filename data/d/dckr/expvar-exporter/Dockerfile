FROM       alpine:3.1
MAINTAINER Johannes 'fish' Ziemke <fish@docker.com> (@discordianfish)
EXPOSE     9111
ENTRYPOINT [ "/bin/expvar_exporter" ]

ENV  GOPATH  /go
ENV  APPPATH $GOPATH/src/github.com/docker-infra/expvar_exporter
COPY . $APPPATH
RUN  apk add --update -t build-deps go git mercurial \
     && cd $APPPATH && go get -d && go build -o /bin/expvar_exporter \
     && apk del --purge build-deps && rm -rf $GOPATH
