FROM ubuntu:14.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get install -y emacs24 ghc libghc-random-dev git tmux openssh-server

RUN mkdir /root/.ssh
ONBUILD ADD authorized_keys /root/.ssh/authorized_keys
ONBUILD RUN chmod 755 /root
ONBUILD RUN chmod 600 /root/.ssh/authorized_keys
ONBUILD RUN chown root:root /root/.ssh/authorized_keys

EXPOSE 22

CMD ["/usr/bin/monit", "-I", "-c", "/etc/monit/monitrc"]


