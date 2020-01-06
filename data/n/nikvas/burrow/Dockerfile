FROM golang:1.11-alpine as builder

ENV DEP_VERSION="0.5.0" \
    BU_VERSION="v1.2.2"

RUN apk add --no-cache git curl gcc libc-dev && \
	curl -L -s https://github.com/golang/dep/releases/download/v${DEP_VERSION}/dep-linux-amd64 -o $GOPATH/bin/dep && \
	chmod +x $GOPATH/bin/dep && \
	mkdir -p $GOPATH/src/github.com/linkedin/Burrow && \
        git clone https://github.com/linkedin/Burrow $GOPATH/src/github.com/linkedin/Burrow && \
        cd $GOPATH/src/github.com/linkedin/Burrow && \
        git checkout tags/${BU_VERSION}

ADD . $GOPATH/src/github.com/linkedin/Burrow/
RUN cd $GOPATH/src/github.com/linkedin/Burrow && \
	dep ensure && \
	go build -o /tmp/burrow .

FROM iron/go
LABEL maintainer="LinkedIn Burrow https://github.com/linkedin/Burrow"

WORKDIR /app
COPY --from=builder /tmp/burrow /app/
ADD /docker-config/burrow.toml /etc/burrow/

CMD ["/app/burrow", "--config-dir", "/etc/burrow"]
