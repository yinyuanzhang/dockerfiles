FROM debian:stable-slim

WORKDIR /root/d3c
COPY ./d3c /root/d3c
RUN cp ld.so.conf /etc/ld.so.conf && ldconfig
RUN chmod +x /root/d3c/d3ccore
RUN echo 'root hard core 88888' >> /etc/security/limits.conf
