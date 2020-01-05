FROM       alpine:latest
MAINTAINER Tim Vaillancourt <tim.vaillancourt@percona.com>
EXPOSE     9104

ENV  GOPATH /go
ENV APPPATH $GOPATH/src/github.com/elarasu/mongodb_exporter
COPY . $APPPATH
RUN apk add --update -t build-deps go git mercurial libc-dev gcc libgcc 
RUN cd $APPPATH && go get -d && go build -o /bin/mongodb_exporter 
RUN apk del --purge build-deps && rm -rf $GOPATH

ENTRYPOINT [ "/bin/mongodb_exporter" ]
