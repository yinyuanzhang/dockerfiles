FROM centos:7

RUN curl -O ftp://fr2.rpmfind.net/linux/fedora/linux/development/rawhide/Everything/x86_64/os/Packages/f/fio-2.14-1.fc26.x86_64.rpm
RUN yum -y --setopt=tsflags=nodocs update && \
	yum -y --nogpgcheck localinstall fio-2.14-1.fc26.x86_64.rpm && \
	yum clean all
RUN rm fio-2.14-1.fc26.x86_64.rpm
RUN mkdir /data

COPY fio.config /data/fio.config

CMD ["fio","/data/fio.config"]
