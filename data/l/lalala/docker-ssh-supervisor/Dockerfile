FROM ubuntu:trusty


# Install packages
ENV DEBIAN_FRONTEND noninteractive


# Set locale (fix the locale warnings)
RUN locale-gen --purge en_US.UTF-8
RUN echo   'LANG="en_US.UTF-8"' > /etc/default/locale
RUN echo   'LANGUAGE="en_US:en"' >> /etc/default/locale


# Set timezone
RUN echo "Asia/Jerusalem"  > /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

RUN rm /etc/apt/sources.list
ADD sources.list /etc/apt/sources.list


RUN apt-get update -y
RUN apt-get install -y openssh-server supervisor 
#software-properties-common python python-software-properties g++ make curl git




#ssh
#ssh configs
RUN mkdir /root/.ssh
RUN mkdir /var/run/sshd

ADD sshkey.pub /root/.ssh/authorized_keys
RUN chown root:root /root/.ssh/authorized_keys
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config


#supervisor configs
RUN mkdir -p /var/log/supervisor
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf



EXPOSE  22
#VOLUME ["/home/lalala/docker-manager/mesanenet-server/volumes/supervisor"]
CMD env | grep _ >> /etc/environment && /usr/bin/supervisord
