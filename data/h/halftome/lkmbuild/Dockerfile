FROM ubuntu
WORKDIR /root

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y install build-essential libelf-dev

CMD apt-get update && apt-get -y install linux-headers-${kernel} && make -C /lib/modules/${kernel}/build M=$(pwd) modules