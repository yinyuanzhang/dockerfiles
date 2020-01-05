From alpine:3.3

RUN apk update && \
    apk add curl && \
    curl -L -o glibc-2.21-r2.apk \ 
      "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-2.21-r2.apk" && \
    curl -L -o glibc-bin-2.21-r2.apk \
      "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-bin-2.21-r2.apk" && \
    apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \
    rm -f glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \
    /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \
    curl https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz | tar xzf - -C / && \
    mv /go /goroot && \
    mkdir /gopath && \
    mkdir /gopath/src && \
    mkdir /gopath/bin && \
    mkdir /gopath/pkg


ENV GOROOT=/goroot \
    GOPATH=/gopath \
    GOBIN=/gopath/bin \
    PATH=${PATH}:/goroot/bin:/gopath/bin
