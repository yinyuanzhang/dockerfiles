FROM centos:centos7

ADD nginx.repo /etc/yum.repos.d/nginx.repo
RUN yum -y install \
	nginx-1.8.* \
	make-3.82* \
	openssl-1.0.* \
    && yum clean all

# add startup script
ADD startup.sh /startup.sh
RUN chmod 755 /startup.sh

VOLUME ["/etc/nginx"]
VOLUME ["/var/www"]

EXPOSE 80 443

# CMD ["nginx", "-g", "daemon off;"]
CMD /startup.sh
