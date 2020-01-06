FROM debian:latest
LABEL maintainer "Hiromu Ochiai <otiai10@gmail.com>"

RUN apt-get update -qq
RUN apt-get install -y -q tesseract-ocr tesseract-ocr-jpn

ADD ./main.sh /

ENTRYPOINT /main.sh
