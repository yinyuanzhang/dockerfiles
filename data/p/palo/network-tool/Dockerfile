FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
  dnsutils \
  inetutils-ping \
  netcat \
  nmap \
  postgresql-client \
  telnet

RUN useradd --uid=1001 tool
USER tool


