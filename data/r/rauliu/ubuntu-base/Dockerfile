FROM       ubuntu:14.04.3
MAINTAINER Raul Liu "https://github.com/rauliu"

# Set locales
RUN locale-gen en_GB.UTF-8
ENV LANG en_GB.UTF-8
ENV LC_CTYPE en_GB.UTF-8

RUN apt-get update

RUN apt-get install -y openssh-server supervisor
RUN mkdir /var/run/sshd

RUN echo 'root:root' |chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

ADD supervisord.conf /etc/supervisor/
ADD sshd.conf /etc/supervisor/conf.d/

EXPOSE 22

CMD ["supervisord", "-n"]
