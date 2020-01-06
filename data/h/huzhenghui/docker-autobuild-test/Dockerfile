FROM alpine

WORKDIR /FromDockerAutobuild

RUN apk add axel && \
    axel -n 1 https://vagrantcloud.com/archlinux/boxes/archlinux/versions/2020.01.03/providers/virtualbox.box && \
    ls -l
