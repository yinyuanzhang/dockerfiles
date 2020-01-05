FROM ubuntu:14.04

RUN apt-get update -y;\
    apt-get upgrade -y;\
    apt-get install libfontconfig1 libxrender1 -y;\
    apt install libxext6;

RUN mkdir -p /wkhtmltopdf

WORKDIR /wkhtmltopdf

ADD wkhtmltox-linux-amd64_0.12.0-03c001d.tar.xz .

RUN mv wkhtmltox/bin/wkhtmltopdf /usr/bin/
