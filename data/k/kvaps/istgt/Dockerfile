FROM ubuntu:16.04
RUN apt-get -y update \
 && apt-get -y install istgt \
 && apt-get -y clean
ENTRYPOINT [ "/usr/sbin/istgt", "-D" ]
