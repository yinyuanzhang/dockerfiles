FROM python:3.7.3-slim-stretch

RUN apt-get update && \
    apt-get install \
      curlftpfs \
      procps \
      telnet \
      less \
      vim \
    --yes && \
    apt-get clean 
