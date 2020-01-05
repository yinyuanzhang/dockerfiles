FROM ubuntu:rolling
RUN apt update
RUN apt-get dist-upgrade -y
RUN apt-get install iperf3 -y
ENTRYPOINT ["iperf3"]
