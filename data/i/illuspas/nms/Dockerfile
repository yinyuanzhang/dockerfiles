FROM frolvlad/alpine-glibc
RUN wget https://github.com/NodeMedia/NodeMediaServer/releases/download/v3.2.5/nms-linux-amd64-20191229.tar.gz -O - | tar xz
EXPOSE 1935 8000 8443 6935/udp
WORKDIR nms-linux-amd64
CMD ["./nms"]
