FROM centos:7
MAINTAINER xyfan@live.it

COPY /libcent/ /usr/local/lib/

COPY om.conf /etc/ld.so.conf.d/

RUN ldconfig

CMD ["/bin/bash"]
