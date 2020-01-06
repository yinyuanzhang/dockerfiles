FROM ubuntu:14.04.5
MAINTAINER Docker Anke <anke950@gmail.com>
RUN apt-get --quiet --quiet update && \
	apt-get --quiet --quiet upgrade --assume-yes && \
	apt-get --quiet --quiet install openssh-server nano --assume-yes
RUN mkdir /var/run/sshd && \
	echo 'root:Password' | chpasswd && \
	sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config && \
# SSH login fix. Otherwise user is kicked off after login
	sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
# expose Secure Shell port
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
