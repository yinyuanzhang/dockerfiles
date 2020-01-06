FROM golang:1.9.2-alpine
ARG VERSION=v1.3.10
RUN apk add --no-cache git 
RUN apk add --update openssl
WORKDIR /go/src/github.com/hacdias/filemanager
RUN wget https://github.com/hacdias/filemanager/archive/${VERSION}.tar.gz
RUN tar -xvf ${VERSION}.tar.gz --strip 1
RUN go get ./...
WORKDIR /go/src/github.com/hacdias/filemanager/cmd/filemanager
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -ldflags "-X main.version=${VERSION}"

FROM alpine:latest 
MAINTAINER "Levent SAGIROGLU" <LSagiroglu@gmail.com>
# Henrique Dias - Web File Manager https://github.com/hacdias/filemanager
RUN apk update && \
    apk upgrade && \
    apk add --update openssl && \
    apk add --update tzdata && \    
    apk add ca-certificates && \
	   update-ca-certificates && \
    cp /usr/share/zoneinfo/Europe/Istanbul /etc/localtime && \
    echo "Europe/Istanbul" >  /etc/timezone && \
    apk del tzdata
    
VOLUME /srv 
ENV FM_ROOT "/" 
COPY entrypoint.sh /bin/entrypoint.sh 
COPY --from=0 /go/src/github.com/hacdias/filemanager/cmd/filemanager/filemanager /bin/filemanager 
COPY README.md /srv/README.md 
EXPOSE 80 
ENTRYPOINT ["/bin/entrypoint.sh"]
