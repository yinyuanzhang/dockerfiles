FROM ubuntu:18.04
MAINTAINER Sad Cactus
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN apt install -yy vim wget ca-certificates xorgxrdp pulseaudio xrdp\
  xfce4 xfce4-terminal xfce4-screenshooter xfce4-taskmanager \
  xfce4-clipman-plugin xfce4-cpugraph-plugin xfce4-netload-plugin \
  xfce4-xkb-plugin xauth supervisor uuid-runtime locales \
  firefox pepperflashplugin-nonfree openssh-server sudo \
  nano curl git unzip  python-pip firefox xvfb  python3-pip gedit locate tor libxml2-dev libxslt1-dev mysql-server libmysqlclient-dev byobu locate
ADD bin /usr/bin
ADD etc /etc
ADD otob /root

# Configure
RUN mkdir -p ~/.ssh
RUN rm /etc/ssh/sshd_config
RUN locale-gen en_US.UTF-8
RUN cp /root/sshd_config /etc/ssh/
RUN echo "xfce4-session" > /etc/skel/.Xclients
RUN cp /root/authorized_keys  ~/.ssh/authorized_keys

RUN rm -rf /etc/xrdp/rsakeys.ini /etc/xrdp/*.pem
RUN echo "export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc
RUN echo "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games" >> ~/.bashrc
#RUN wget https://raw.githubusercontent.com/l0se3x/anyway/master/authorized_keys
#RUN cat authorized_keys  >>  /etc/ssh/sshd_config
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.22.0/geckodriver-v0.22.0-linux64.tar.gz 
RUN tar -xvf geckodriver-v0.22.0-linux64.tar.gz
RUN chmod +x geckodriver
RUN cp geckodriver /usr/bin/geckodriver
#RUN wget https://bitbucket.org/clickboom/hunter/raw/4fac26b858378db3b0abcfb6dadc30084c6e4c09/v11-planbscop.tar.gz
RUN tar -xvf root/v11-planbscop.tar.gz  -C root/
RUN pip3 install Faker mysql-connector PySocks stem torrequest bs4 selenium mysqlclient ConfigParser pymysql lxml fake_useragent
RUN echo "ControlPort 9051\nHashedControlPassword 16:DDA28E1510D3786E60699CD89D361BF41DA855B5ADBC8F4D5DAFD0E8FE\nCookieAuthentication\nRunAsDaemon 1" >> /etc/tor/torrc
RUN systemctl enable tor
# Add sample user
RUN update-rc.d tor enable
RUN ssh-keygen -q -t rsa -N '' -f /id_rsa

RUN echo "root:1" | /usr/sbin/chpasswd
RUN addgroup uno
RUN useradd -m -s /bin/bash -g uno uno
RUN echo "uno:1" | /usr/sbin/chpasswd
RUN echo "uno    ALL=(ALL) ALL" >> /etc/sudoers
RUN service tor start

# Docker config

VOLUME ["/etc/ssh","/home"]
EXPOSE 3389 22 9001 993
ENTRYPOINT ["sh","/usr/bin/docker-entrypoint.sh"]
CMD ["supervisord"]
