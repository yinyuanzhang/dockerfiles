FROM debian:latest
MAINTAINER Kunger <fssbbskefu@gmail.com>
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:root' |chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN mkdir /root/.ssh && \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAs9mMr2utH0yeawDr8yEQLRNXmQxfvUnvuzdAWT9rI20tK5u6f79LkF2OoyBwJfTrBULOxuf6H5hmYNZ2ubvf7chFggr0dN5JYlBrNpkSOozUVcmx0pWolndGWO1NsPS1h1GGC5pqVU/Gn4tZLGdx/geg+bgMIWBiT8hCdq2Q8WDAhZYupuCRSSoYiPnBZMPu9BsfsFF6MvdQ3bO81vfoVgzIX3UUf7HsbWa7CxNmPKYVxq438MW0dwXytePkIiTK13MogIn5Vt0AE8OSF1XNMoYTrHWEJlShGlsxOn6pjtTBYs62XkbLGhZZuTcz1JuTSbnm9fXeiQVptY/qqF1oCQ== OpenSSH-rsa-import-011318" > /root/.ssh/authorized_keys
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
EXPOSE 22
CMD    ["/usr/sbin/sshd", "-D"]
