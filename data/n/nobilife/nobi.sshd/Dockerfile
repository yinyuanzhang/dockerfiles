FROM alpine:3.9
MAINTAINER Niels Avonds <niels@nobi.life>

RUN apk --update add --no-cache openssh bash \
  && sed -i s/#PermitRootLogin.*/PermitRootLogin\ yes/ /etc/ssh/sshd_config \
  && echo "root:root" | chpasswd \
  && rm -rf /var/cache/apk/*
RUN sed -ie 's/#Port 22/Port 22/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_key/HostKey \/etc\/ssh\/ssh_host_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_rsa_key/HostKey \/etc\/ssh\/ssh_host_rsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_dsa_key/HostKey \/etc\/ssh\/ssh_host_dsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ecdsa_key/HostKey \/etc\/ssh\/ssh_host_ecdsa_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#HostKey \/etc\/ssh\/ssh_host_ed25519_key/HostKey \/etc\/ssh\/ssh_host_ed25519_key/g' /etc/ssh/sshd_config
RUN sed -ir 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
RUN sed -ir 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
RUN sed -ir 's/AllowTcpForwarding no/AllowTcpForwarding yes/g' /etc/ssh/sshd_config
RUN sed -ir 's/#PermitTunnel no/PermitTunnel yes/g' /etc/ssh/sshd_config

RUN /usr/bin/ssh-keygen -A
RUN ssh-keygen -t rsa -b 4096 -f  /etc/ssh/ssh_host_key

COPY authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

EXPOSE 22
CMD ["/usr/sbin/sshd","-D"]
