FROM centos
EXPOSE 80
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
RUN yum install wget -y
WORKDIR /opt
RUN wget https://www.linuxdot.net/down/jexus-6.1-x64.tar.gz
RUN tar zxvf jexus-6.1-x64.tar.gz && rm -f jexus-6.1-x64.tar.gz
WORKDIR /var/www/default
CMD ["/opt/jexus/jwss"]
