FROM golang:1.13.1-alpine3.10 AS build

RUN apk add --no-cache make bash

# ADD https://github.com/TykTechnologies/tyk/archive/master.tar.gz .
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN wget https://github.com/TykTechnologies/tyk/archive/master.tar.gz -O - \
    | tar xzf -

WORKDIR /go/tyk-master
RUN make build-linux

RUN /go/tyk-master/tyk --version

FROM scratch
COPY --from=build /go/tyk-master/tyk .
