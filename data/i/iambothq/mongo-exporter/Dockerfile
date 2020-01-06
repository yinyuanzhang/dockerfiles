FROM golang:1.12

ENV APPPATH $GOPATH/src/github.com/percona/mongodb_exporter
WORKDIR $APPPATH

RUN git clone "https://github.com/percona/mongodb_exporter" "$APPPATH"
RUN git checkout v0.7.0
RUN go get -d && go build -o /mongodb_exporter && rm -rf "$GOPATH"

EXPOSE 9216

ENTRYPOINT [ "/mongodb_exporter" ]