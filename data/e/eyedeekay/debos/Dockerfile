FROM debian:sid
ARG GOPATH=/opt/src/gocode
ENV GOPATH=/opt/src/gocode
RUN apt-get update
RUN apt-get install -y golang git libglib2.0-dev libostree-dev qemu-system-x86 \
     qemu-user-static debootstrap busybox systemd-container
RUN go get -u github.com/go-debos/debos/cmd/debos
RUN adduser --disabled-password --gecos 'debos,,,,' debos
CMD /opt/src/gocode/bin/debos
