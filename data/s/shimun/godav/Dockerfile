FROM golang AS build

RUN cd $GOPATH && mkdir -p {src,bin,pkg} && mkdir -p src/github.com/hacdias/ && cd src/github.com/hacdias/ && git clone https://github.com/shimunn/webdav.git

RUN go get -d github.com/shimunn/webdav/

RUN go install github.com/shimunn/webdav/ && cp $GOPATH/bin/webdav /usr/bin/

FROM frolvlad/alpine-glibc

RUN apk --no-cache add bash && mkdir /davroot

COPY --from=build /usr/bin/webdav /usr/bin/webdav

ADD entrypoint.sh /entrypoint.sh 

ADD config.yaml /etc/webdav/config.yaml

RUN chmod +x /entrypoint.sh

VOLUME /davroot

EXPOSE 8082

ENTRYPOINT /entrypoint.sh

