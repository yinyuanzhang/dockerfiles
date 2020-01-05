FROM sbilo/stellar-builder:latest as builder

FROM ubuntu:latest

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update
RUN apt-get install -y ca-certificates 
COPY --from=builder /go/bin/bifrost /bin 
ENTRYPOINT ["bifrost","server","--config","/etc/bifrost/bifrost.cfg"]

