FROM golang:latest

# Necessary to avoid dependency issues
# It seems the usage of a pkg/ directory is deprecated?
RUN apt-get update && apt-get -y install p7zip-full mingw-w64  \
    &&  go get -u github.com/fogleman/serve \
    && go get -u "github.com/fatih/color" \
    && go get -u "github.com/Ne0nd0g/merlin/pkg/banner" \
    && go get -u "github.com/Ne0nd0g/merlin/pkg/servers/http2" \
    && go get -u "github.com/Ne0nd0g/merlin/pkg/logging" \
    && go get -u "github.com/Ne0nd0g/merlin/pkg/core" \
    && go get -u "github.com/Ne0nd0g/merlin/pkg/cli" \
    && go get -u "github.com/Ne0nd0g/merlin/pkg" \
    && git clone https://github.com/Ne0nd0g/merlin.git

WORKDIR merlin

RUN mkdir -p /go/merlin/data/x509/ \
    && openssl req -subj '/C=US/ST=New York/L=Brooklyn/O=example/CN=example.com' -new -newkey rsa:4096 -days 3650 -nodes -x509 -keyout /go/merlin/data/x509/server.key -out /go/merlin/data/x509/server.crt

EXPOSE 443
EXPOSE 8000

RUN make all && find . -type f -name "*-Linux-x64" -exec cp {} /go/merlin/ \;
# Either launch C2 or start a Simple HTTP server to the cert & compiled files
ENTRYPOINT [ "bash", "-c" ]
CMD [ "serve -dir /go/merlin/data/temp/"]
