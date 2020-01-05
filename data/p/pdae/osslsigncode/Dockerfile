FROM debian:latest

RUN apt-get update && apt-get install -y osslsigncode

COPY sign /usr/local/bin/
RUN chmod +x /usr/local/bin/sign
