FROM debian:9.8-slim

ENV CORE_VERSION 10.3.0rc2-837-de204d71
ENV CONFD_VERSION 0.16.0

EXPOSE 11625
EXPOSE 11626

ADD install /
RUN /install

ADD confd /etc/confd
ADD start /

CMD ["/start"]
