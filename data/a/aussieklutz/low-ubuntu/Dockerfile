FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y sudo
RUN apt-get install -y iputils-*
RUN apt-get install -y wget
RUN apt-get install -y nano
RUN apt-get install -y dnsutils
RUN apt-get install -y python
RUN apt-get install -y git 
RUN apt-get install -y cron
RUN apt-get install -y nmap
RUN apt-get install -y net-tools
RUN apt-get install -y vim
RUN apt-get install -y netcat
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
RUN echo root:toor | chpasswd
RUN echo "* ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers
RUN chmod 777 /etc/passwd
RUN chmod 777 /etc/group
USER appuser
RUN true
ENTRYPOINT ["tail", "-f", "/dev/null"]
