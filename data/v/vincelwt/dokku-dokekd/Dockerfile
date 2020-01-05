FROM ubuntu:14.04

RUN apt-get update
RUN apt-get install -y git make curl software-properties-common sudo wget man openssh-server iptables ca-certificates lxc help2man

RUN curl -sSL https://get.docker.com/ | sh

VOLUME ["/home/dokku","/var/lib/docker","/var/lib/dokku/data","/var/lib/dokku/services"]

RUN apt install -y psmisc python-pip
RUN pip install --upgrade pip setuptools
RUN pip install flask pyopenssl Flask-BasicAuth boto

ENV HOME /root
WORKDIR /root
ADD ./monitor.sh /root/monitor.sh
ADD ./setup.sh /root/setup.sh
ADD ./wrapdocker /usr/local/bin/wrapdocker
RUN chmod +x /usr/local/bin/wrapdocker
RUN chmod +x /root/monitor.sh
RUN touch /root/.firstrun

EXPOSE 22
EXPOSE 80
EXPOSE 443
EXPOSE 5657

CMD ["bash", "/root/setup.sh"]