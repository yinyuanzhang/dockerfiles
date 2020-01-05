FROM alpine:latest

MAINTAINER Aasif Shaikh (acloudiator@gmail.com)

RUN apk --update add iperf3 \
    && rm -rf /var/cache/apk/* \
    && adduser -S iperf

USER iperf

#Expose ports    
EXPOSE 5201

ENTRYPOINT ["iperf3"]

CMD ["-s"]
