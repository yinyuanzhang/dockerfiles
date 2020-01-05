FROM debian:jessie

# Install openssh, git, sshpass
RUN apt-get update && apt-get install -y openssh-server sshpass curl git ruby ruby-dev build-essential
RUN mkdir /var/run/sshd

ENV ROOT_PASSWORD root
RUN echo "root:${ROOT_PASSWORD}" | chpasswd

RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Install sass and compass
RUN gem install sass
RUN gem update --system && gem install compass
RUN gem uninstall bundler -x || exit 0
RUN gem install bundler -v 1.16.0 --force
RUN bundle _1.16.0_ install || exit 0

ADD start.sh /start.sh
RUN chmod 777 /start.sh

EXPOSE 22
ENTRYPOINT /start.sh
