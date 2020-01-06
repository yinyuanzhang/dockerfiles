# Compile
FROM golang:1.10 as compile

COPY . /usr/local/go/src/bitbucket.org/faide/confnest
WORKDIR /usr/local/go/src/bitbucket.org/faide/confnest
RUN go get -u github.com/kardianos/govendor
RUN govendor sync
RUN go build bitbucket.org/faide/confnest

# Package
FROM debian

COPY --from=compile /usr/local/go/src/bitbucket.org/faide/confnest/confnest /usr/local/bin

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -yq git mercurial

CMD confnest
