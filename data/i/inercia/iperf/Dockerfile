FROM gliderlabs/alpine:3.1
MAINTAINER Alvaro Saurin <alvaro.saurin@gmail.com>
RUN apk --update add iperf
EXPOSE 5001/tcp 5001/udp
ENTRYPOINT ["/usr/bin/iperf"]
CMD ["-s"]