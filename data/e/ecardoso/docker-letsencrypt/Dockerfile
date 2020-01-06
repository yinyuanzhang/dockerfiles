FROM ubuntu:latest

RUN apt-get update && apt-get -y install git bc

RUN git clone https://github.com/letsencrypt/letsencrypt /opt/letsencrypt

RUN mkdir /webroot

VOLUME /webroot
VOLUME /etc/letsencrypt

WORKDIR /opt/letsencrypt

ENTRYPOINT ["./letsencrypt-auto", "certonly", "-a", "webroot", "--webroot-path=/webroot"]

CMD ["-d", "example.com"]
