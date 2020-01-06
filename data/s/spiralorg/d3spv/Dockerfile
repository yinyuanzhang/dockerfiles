FROM debian:stable-slim

WORKDIR /root/d3spv
COPY ./d3spv /root/d3spv
RUN cp ld.so.conf /etc/ld.so.conf && ldconfig
RUN chmod +x /root/d3spv/D3_SPV_CLIENT
