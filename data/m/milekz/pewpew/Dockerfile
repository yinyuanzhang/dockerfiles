FROM alpine

RUN apk update --update && apk add --no-cache musl-dev go git dep gcc && \
git clone https://github.com/milekz/pewpew.git /root/go/src/pewpew && \
cd /root/go/src/pewpew && \
dep ensure && \
go build -o /usr/local/bin/pewpew main.go && \
apk del musl-dev go git dep gcc && cd /

WORKDIR /root/go/src/pewpew

CMD [ "/usr/local/bin/pewpew" ]
