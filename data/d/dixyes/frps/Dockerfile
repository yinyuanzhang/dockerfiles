
FROM golang:alpine AS builder
# only for slow repo in china
#RUN sed -i 's/dl-cdn\.alpinelinux\.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories 
RUN apk --no-cache --no-progress add make
WORKDIR /go/src/github.com/fatedier/frp
COPY . .
RUN make frps

FROM alpine:latest
WORKDIR /frp
COPY --from=builder /go/src/github.com/fatedier/frp/bin/frps /usr/local/bin
ENTRYPOINT [ "frps" ]
