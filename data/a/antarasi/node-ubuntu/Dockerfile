FROM ubuntu:16.04
MAINTAINER ANTARA IT Systems "contact@antara.pl"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
    && apt-get -qq update \
    && apt-get -y install sudo git curl openssh-server \
    && mkdir /var/run/sshd

RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - \
    && apt-get update && apt-get install -y nodejs \
    && npm install npm@5.2.0 -g

RUN apt-get install -y ufw

RUN node -v && npm -v

RUN useradd -ms /bin/bash ubuntu \
    && echo 'root:root' | chpasswd \
    && echo 'ubuntu:ubuntu' | chpasswd \
    # SSH login fix. Otherwise user is kicked off after login
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

#allow services to start automatically from this point
#https://askubuntu.com/questions/365911/why-the-services-do-not-start-at-installation
RUN printf '#!/bin/sh\nexit 0\n' > /usr/sbin/policy-rc.d

USER ubuntu

RUN ssh-keygen -q -f ~/.ssh/id_rsa -t rsa -b 4096 -N '' -C 'ubuntu@ubuntu:16.04'

USER root

CMD ["/bin/bash"]
VOLUME ["/root"]

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]