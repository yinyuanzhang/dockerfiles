# https://github.com/sjitech/ubuntu-with-utils/blob/master/Dockerfile
FROM osexp2000/ubuntu-with-utils

USER root

RUN apt-get update && apt-get -y install build-essential gcc g++ gdb make \
    automake autopoint libtool pkg-config bison gettext

USER devuser
