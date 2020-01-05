FROM golang as builder

RUN go get -u -v github.com/Ronmi/ynit
RUN go install github.com/Ronmi/ynit

FROM debian:oldstable
MAINTAINER Ronmi Ren <ronmi.ren@gmail.com>

COPY --from=builder /go/bin/ynit /usr/local/bin/
RUN mkdir /etc/ynit

CMD ["/usr/local/bin/ynit"]
