FROM golang:1.4.2

ADD ./ /go/src/github.com/qurius-inc/gitrelease

RUN mkdir /releases
WORKDIR /releases

RUN go get -v github.com/qurius-inc/gitrelease/...
RUN go install github.com/qurius-inc/gitrelease

# this entrypoint makes the docker image more usable
# as a standalone app, but you end up needing to
# override the entrypoint during debugging.
# Leaving it disabled for now.

#ENTRYPOINT gitrelease