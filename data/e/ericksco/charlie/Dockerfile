FROM docker.io/centos:latest

ARG build_date

LABEL name="CentOS Custom Image" \
    vendor="CentOS" \
    build-date="2019032100" \
    maintainer="ericksco74@gmail.com"

EXPOSE 80
#RUN yum-config-manager --setopt=proxy=http://10.10.0.1:3128 --save
RUN yum install -y bash less
#RUN yum install -y bash vim less
RUN yum install -y net-tools iproute nmap-ncat lsof bind-utils
RUN yum install -y wget curl elinks 
RUN yum install -y httpd ssh

ENTRYPOINT ["/usr/sbin/httpd"]
