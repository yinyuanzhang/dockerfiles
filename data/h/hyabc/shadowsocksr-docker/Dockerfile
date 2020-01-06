FROM ubuntu:16.04

RUN apt update
RUN apt install -y libsodium18 python-pip
RUN pip --no-cache-dir install https://github.com/shadowsocksr-backup/shadowsocksr/archive/manyuser.zip

EXPOSE 80
ENTRYPOINT ["/usr/bin/ssserver", "-s", "0.0.0.0", "-p", "80", "-k", "passwd123456", "-m", "chacha20", "-o", "http_simple"]
