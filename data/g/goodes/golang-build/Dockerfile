FROM golang:1.10.3-alpine
RUN apk add curl git gcc libc-dev

# Pin to 0.4.1 to be same version as fedora 28 godep package
RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | DEP_RELEASE_TAG=v0.4.1 sh