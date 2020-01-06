FROM fedora:26

LABEL maintainer="Lars Melwyn <melwyn (at) dtu.dk>"

USER root

RUN adduser user && dnf install git rsync pandoc -y && dnf clean all 

USER user

RUN cd /home/user; git clone https://github.com/markdownreveal/example.git; pip3 install --user  markdownreveal

WORKDIR /home/user/example

ENTRYPOINT ~/.local/bin/mdr presentation.md --port 8123 --host 0.0.0.0
