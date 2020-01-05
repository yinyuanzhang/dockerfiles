FROM debian:latest
RUN apt-get update -y
RUN apt-get install quagga -y
ADD ./conf /etc/quagga/
CMD /etc/init.d/quagga start