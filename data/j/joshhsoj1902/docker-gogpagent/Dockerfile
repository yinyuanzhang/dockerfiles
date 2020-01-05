FROM golang:latest@sha256:544b2d0378d9de9a8ade9cebd9a333e60cc8343f9d3dd01ccccfc4c1395ce132
RUN mkdir -p /go/src/github.com/joshhsoj1902/docker-gogpagent
ADD . /go/src/github.com/joshhsoj1902/docker-gogpagent/
WORKDIR /go/src/github.com/joshhsoj1902/docker-gogpagent
RUN cp /go/src/github.com/joshhsoj1902/docker-gogpagent/overrides/server.go /go/src/github.com/joshhsoj1902/docker-gogpagent/vendor/github.com/divan/gorilla-xmlrpc/xml/server.go
RUN env
RUN ls -ltr
RUN make build
ENV USERNAME=agent
HEALTHCHECK CMD curl --fail http://localhost:12679/health || exit 1  

CMD ["/go/src/github.com/joshhsoj1902/docker-gogpagent/main"]
