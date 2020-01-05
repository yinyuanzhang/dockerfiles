FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
  git \
  vim \
  dnsutils \
  curl \
  net-tools \
  wget \
  openssh-server

######################
## SECURITY WARNING ##
######################
# This expose ssh root login with password!
RUN mkdir /var/run/sshd
WORKDIR /etc/ssh
RUN sed -ibk "s/^\#\s*PasswordAuthentication.*$/PasswordAuthentication yes/" sshd_config
RUN sed -ibk "s/^\#\s*PermitRootLogin.*$/PermitRootLogin yes/" sshd_config
RUN service ssh stop

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

COPY docker-entrypoint.sh /

EXPOSE 22/TCP

WORKDIR /
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["start-ssh"]
