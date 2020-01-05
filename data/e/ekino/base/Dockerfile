# --- BASE ---

FROM ubuntu:trusty
MAINTAINER Matthieu Fronton <fronton@ekino.com>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

# prerequisites
RUN apt-get update
RUN apt-get install -y curl supervisor vim unzip

# cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

# configure
ENV TIMEZONE Europe/Paris
RUN echo $TIMEZONE > /etc/timezone && dpkg-reconfigure tzdata

RUN groupadd -g 42310 ekino && useradd -g 42310 -u 42310 -d /home/ekino -m -s /bin/bash ekino

ADD supervisord.conf /etc/supervisor/conf.d/base.conf
ADD vimrc /root/.vimrc

# startup
RUN mkdir -p /start.d
ADD base.sh /start.d/00-base
ADD supervisord.sh /start.d/99-supervisord

ADD start.sh /start.sh
CMD ["/start.sh"]
