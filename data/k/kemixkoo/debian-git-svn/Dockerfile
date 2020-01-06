FROM debian:buster-slim
MAINTAINER Kemix Koo <kemix_koo@163.com>

ENV DEBIAN_FRONTEND noninteractive

# install git and ssh
RUN apt-get -y update && apt-get -y install wget curl git subversion nano openssh-server \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/man/?? /usr/share/man/??_*

# add gitconfig
ADD .gitconfig /root

# set alias for nano
RUN echo "alias nano='export TERM=xterm && nano'" >> /root/.bashrc

CMD git --version && svn --version && nano --version
