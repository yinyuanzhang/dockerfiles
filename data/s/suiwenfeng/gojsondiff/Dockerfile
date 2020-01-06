FROM golang
ENV BEFORE "http://stage.abc.shein.com"
ENV AFTER "http://srch-goodslist-master.stage:8080"
WORKDIR $GOPATH/src/bitbucket.org/wenfengsui/gojsondiff
COPY . .
RUN go get -d -v ./...
RUN go install -v ./...
EXPOSE 8888
ENTRYPOINT gojsondiff -m web -b "${BEFORE}" -a "${AFTER}"