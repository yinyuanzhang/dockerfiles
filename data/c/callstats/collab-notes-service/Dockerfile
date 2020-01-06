FROM golang:1.11-alpine

# configure installation variables
ARG SERVICE_VERSION=UNDEFINED
ENV SERVICE_VERSION=${SERVICE_VERSION}

RUN apk add --no-cache bash
# Add required files, ignores test
WORKDIR /go/src/github.com/callstats-io/collab-notes-service/
# TODO rm vendor
ADD vendor/ vendor/
ADD scripts/docker/install_service.sh install_service.sh
ADD main.go main.go
ADD cmd/ cmd/
ADD src/ src/
RUN bash ./install_service.sh $SERVICE_VERSION github.com/callstats-io/collab-notes-service/src/config

CMD /go/bin/collab-notes-service
