FROM debian:stretch

MAINTAINER simodj_h@etna-alternance.net

RUN DEBIAN_FRONTEND=noninteractive apt-get update -y\
 	&& apt-get install -y emacs vim nano git subversion curl wget perl python3 python3-pip build-essential openssh-server tree zip sudo locales bash-completion apt-transport-https

EXPOSE 22

RUN useradd user -s /bin/bash \
	&& echo "user:user" | chpasswd \
	&& mkdir /home/user \
	&& chown user:user /home/user \
	&& addgroup user sudo \
	&& true

RUN sed -i "s/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/g" /etc/locale.gen
RUN locale-gen 
RUN mkdir -p /var/run/sshd && sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config \
    && sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && touch /root/.Xauthority

COPY --chown=user fichiers_ressources/bashrc.sh /home/user/.bashrc