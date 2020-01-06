FROM centos:7

ADD /contents /

RUN yum -y install epel-release

RUN yum groupinstall "Server with GUI" "Xfce" -y

RUN yum -y install wget curl git firefox openssh-server passwd x2goserver-xsession google-chrome-stable; yum clean all

RUN yum install java-1.8.0-openjdk-devel.x86_64 -y

ADD ./start.sh /start.sh

RUN mkdir /var/run/sshd

RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' 

RUN chmod 755 /start.sh

RUN ./start.sh

RUN mkdir /home/user/idea  && \
    wget -qO- https://download.jetbrains.com/idea/ideaIU-2018.2.tar.gz | tar zx --strip 1 -C /home/user/idea

EXPOSE 22

ENTRYPOINT ["/usr/sbin/sshd", "-D"]
