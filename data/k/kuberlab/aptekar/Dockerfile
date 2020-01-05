FROM golang:1.9.4

RUN mkdir /glide \
    && cd /glide \
    && wget https://github.com/Masterminds/glide/releases/download/v0.12.3/glide-v0.12.3-linux-386.tar.gz \
    && tar -zxf glide-v0.12.3-linux-386.tar.gz \
    && cp linux-386/glide ./ \
    && rm glide-v0.12.3-linux-386.tar.gz \
    && rm -rf linux-386

RUN mkdir -p "$GOPATH/src/github.com/kuberlab/aptekar"
COPY ./pkg "$GOPATH/src/github.com/kuberlab/aptekar/pkg"
COPY ./aptekar.go "$GOPATH/src/github.com/kuberlab/aptekar/aptekar.go"
COPY ./glide* "$GOPATH/src/github.com/kuberlab/aptekar/"

RUN cd "$GOPATH/src/github.com/kuberlab/aptekar" \
    && /glide/glide install -v \
    && go install -v \
    && rm -rf "$GOPATH/src/github.com/kuberlab/aptekar"

COPY ./swagger-ui "$GOPATH/swagger-ui"

RUN date '+%Y-%m-%d %H:%M:%S' > "$GOPATH/buildtime"

CMD [ "aptekar" ]

EXPOSE 8082
