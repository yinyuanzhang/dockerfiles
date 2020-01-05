FROM docker.io/centos
LABEL Angelo E. Valdez "angeloevaldez@gmail.com"
RUN yum -y update 
RUN yum -y install httpd
RUN yum clean all
EXPOSE 80
EXPOSE 443
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"] 
