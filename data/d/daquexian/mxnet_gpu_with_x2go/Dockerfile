# Start with cuDNN base image
FROM mxnet/python:1.3.1_gpu_cu90_mkl_py3
MAINTAINER daquexian <daquexian566@gmail.com>

# Switch to USTC mirrors. Comment if you are not in China.
RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list

RUN apt-get update 

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y openssh-server xubuntu-desktop 

RUN add-apt-repository ppa:x2go/stable

RUN apt-get update

RUN apt-get install x2goserver x2goserver-xsession pwgen -y

RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g" /etc/ssh/sshd_config

RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix

RUN sed -i "s/mesg n/tty -s \&\& mesg n/" /root/.profile

RUN echo "root:123456" | chpasswd

EXPOSE 22

RUN apt install aria2 -y

RUN aria2c -s16 -x16 https://download-cf.jetbrains.com/python/pycharm-community-2018.3.2.tar.gz

ADD run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]

RUN echo "export PATH=/usr/local/nvidia/bin/:/usr/local/cuda/bin:$PATH" >> /root/.profile
RUN echo "export LD_LIBRARY_PATH=/usr/local/nvidia/lib:/usr/local/nvidia/lib64:$LD_LIBRARY_PATH" >> /root/.profile
RUN echo "source /root/.profile" >> /root/.bashrc
