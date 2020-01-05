FROM alpine

RUN apk update && \
    apk add --no-cache --upgrade \
     iperf3
     
EXPOSE 5201

CMD ["/usr/bin/iperf3","-s"]
