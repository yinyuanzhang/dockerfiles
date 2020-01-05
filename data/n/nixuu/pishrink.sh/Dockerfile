FROM ubuntu:latest
ENV DEBIAN_FRONTEND noninteractive
ADD ./pishrink.sh /home/pishrink.sh
RUN chmod +x /home/pishrink.sh && apt update -y && apt install udev parted -y
WORKDIR /home
ENTRYPOINT [ "/bin/bash", "pishrink.sh", "image.img" ]
