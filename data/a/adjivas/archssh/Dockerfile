FROM base/archlinux
LABEL name="archssh"
MAINTAINER adjivas <adjivas@student.42.fr>
RUN pacman -Syy ;
RUN pacman -S --noconfirm openssh openssl ;
RUN ssh-keygen -A
RUN echo "root:42" | chpasswd
RUN sed -i -e 's/^UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config
ENV HOME /root
ENTRYPOINT ["/usr/sbin/sshd", "-D"]
WORKDIR $HOME
EXPOSE 22
