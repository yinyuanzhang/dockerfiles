FROM dokku32bit/ubuntu-debootstrap:14.04

RUN apt-get update -y && apt-get install --no-install-recommends -y -q wget build-essential ca-certificates git mercurial bzr
RUN mkdir /goroot && wget -qO- https://storage.googleapis.com/golang/go1.4.2.linux-386.tar.gz | tar xvzf - -C /goroot --strip-components=1
RUN mkdir /gopath

ENV GOROOT /goroot
ENV GOPATH /gopath
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin

