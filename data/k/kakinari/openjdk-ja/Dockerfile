FROM kakinari/centos-ja:latest
ARG TARGET=java-1.8.0-openjdk
ENV container docker
RUN yum -y install ${TARGET};\
yum -y upgrade;\
yum -y clean all;\
rm -rf /var/cache/yum/*;
VOLUME /sys/fs/cgroup
CMD /usr/sbin/init
