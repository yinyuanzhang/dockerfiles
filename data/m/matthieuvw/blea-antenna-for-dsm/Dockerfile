FROM debian:jessie

ARG account_name=blea-antenna
ARG account_password=blea-antenna
ARG ssh_port=22000
ARG timezone=Europe/Paris

# Applicatifs

RUN apt-get update && \
	apt-get install -y whois sudo openssh-server bluetooth bluez

# Utilisateurs

RUN	useradd -ms /bin/bash $account_name && \
	echo "$account_name:$account_password" | chpasswd && \
	usermod -aG sudo $account_name && \
	echo "$account_name ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

# SSH configuration

RUN sed -i -e "s/^Port .*/Port $ssh_port/g" /etc/ssh/sshd_config
RUN sed -i -e "s/^#Port .*/Port $ssh_port/g" /etc/ssh/sshd_config

# Date & time

RUN ln -snf /usr/share/zoneinfo/$timezone /etc/localtime && echo "$timezone" > /etc/timezone
RUN sudo dpkg-reconfigure -f noninteractive tzdata

ENTRYPOINT service ssh restart && bash

