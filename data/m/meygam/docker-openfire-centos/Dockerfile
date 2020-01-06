FROM    centos:centos6
MAINTAINER Saravana Kumar Periyasamy <saravanakumar.periyasamy@gmail.com>

RUN     yum install -y initscripts
RUN     yum install -y wget
RUN     wget http://www.igniterealtime.org/downloadServlet?filename=openfire/openfire-3.9.3-1.i386.rpm -O openfire-3.9.3-1.i386.rpm
RUN     rpm -ivh openfire-3.9.3-1.i386.rpm
RUN     yum install -y libldb.i686
#EXPOSE  9090
CMD     service openfire start && tail -f /opt/openfire/logs/info.log


