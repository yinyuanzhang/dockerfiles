FROM igaki/sshmonit

MAINTAINER igaki version:0.1

RUN yum update -y

#Mongodb Install
RUN echo -e "[10gen] \nname=10gen Repository \nbaseurl=http://downloads-distro.mongodb.org/repo/redhat/os/x86_64 \ngpgcheck=0 \nenabled=1" > /etc/yum.repos.d/10gen.repo
RUN yum install -y mongo-10gen mongo-10gen-server

RUN sed -i -e "s/bind_ip=127.0.0.1/bind_ip=0.0.0.0/g" /etc/mongod.conf

ADD ./mongod_monit.conf /etc/monit/conf.d/

RUN chown root:root -R /etc/monit*;chmod 700 /etc/monit.conf

#ssh
EXPOSE 22
#monit
EXPOSE 8001
#mongo
EXPOSE 27017

CMD ["/usr/bin/monit", "-I", "-c", "/etc/monit.conf"]