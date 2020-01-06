FROM buhuipao/centos7-ssh:v0.1.1

MAINTAINER buhuipao <chenhua22@outlook.com>

COPY ./nginx.repo /etc/yum.repos.d/
RUN yum install -y nginx &&\
    rm -f /etc/nginx.conf

COPY ./nginx.conf /etc/nginx/nginx.conf

RUN /usr/sbin/sshd && systemctl enable nginx 
RUN echo -e "#!/bin/bash\n/usr/sbin/sshd\nsystemctl enable nginx\n/usr/sbin/nginx" > /root/init.sh
RUN chmod u+x /root/init.sh

EXPOSE 22 80 443

CMD ["/root/init.sh"]
