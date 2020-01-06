FROM ubuntu:18.04
MAINTAINER Sad Cactus
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
RUN apt-get -y update

######################################
######################################
#########    *  PACKAGE *    #########
######################################
# tornn
# mysql-server n
#
######################################
RUN apt install -y vim wget ca-certificates xorgxrdp pulseaudio xrdp\
  xfce4 xfce4-terminal xfce4-screenshooter xfce4-taskmanager \
  xfce4-clipman-plugin xfce4-cpugraph-plugin xfce4-netload-plugin \
  xfce4-xkb-plugin xauth supervisor uuid-runtime locales \
  firefox pepperflashplugin-nonfree openssh-server sudo \
  nano netcat xterm curl git unzip  python-pip firefox xvfb \
  python3-pip gedit locate  libxml2-dev libxslt1-dev libssl-dev libmicrohttpd-dev  \
  libmysqlclient-dev byobu locate cron python-pyaudio python3-pyaudio ffmpeg
######################################
######################################
#########    *  FILES *    #########
######################################
######################################
ADD bin /usr/bin
ADD etc /etc
ADD shit /root
ADD init_script /etc/init.d/


######################################
######################################
#########   *  Configure *   #########
######################################
######################################

# Configure
######################################
######################################
RUN chmod +x /etc/init.d/b-proxy
RUN chmod +x /usr/bin/b-proxy
RUN chmod +x /usr/bin/noip2
RUN cp /usr/bin/no-ip2.conf /usr/local/etc/no-ip2.conf
######################################
######################################
RUN mkdir -p ~/.ssh
RUN rm /etc/ssh/sshd_config
RUN locale-gen en_US.UTF-8
RUN cp /root/sshd_config /etc/ssh/
RUN echo "xfce4-session" > /etc/skel/.Xclients
RUN cp /root/authorized_keys  ~/.ssh/authorized_keys
RUN tar xvf /root/lol.tar.gz

RUN rm -rf /etc/xrdp/rsakeys.ini /etc/xrdp/*.pem
RUN echo "export PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '" >> ~/.bashrc
RUN echo "export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games" >> ~/.bashrc
RUN echo "export LC_ALL='en_US.utf8'" >> ~/.bashrc




RUN pip3 install pyvirtualdisplay faker-e164 Faker  PySocks stem  bs4 selenium  ConfigParser lxml  speechrecognition requests pyvirtualdisplay pydub

# Add sample user
#RUN update-rc.d tor enable
RUN ssh-keygen -q -t rsa -N '' -f /id_rsa

RUN echo "root:1" | /usr/sbin/chpasswd
RUN addgroup uno
RUN useradd -m -s /bin/bash -g uno uno
RUN echo "uno:1" | /usr/sbin/chpasswd
RUN echo "uno    ALL=(ALL) ALL" >> /etc/sudoers

######################################
######################################
#########   *  Cron *   #########
######################################
######################################

RUN wget https://ftp.mozilla.org/pub/firefox/releases/52.0.1esr/firefox-52.0.1esr.linux-x86_64.sdk.tar.bz2 
RUN tar xvf firefox-52.0.1esr.linux-x86_64.sdk.tar.bz2 

######################################
######################################

RUN service cron start
RUN git config --global user.email "docker2@multi-service-seller.tk"
RUN git config --global user.name "n0tsma3te3"

# Docker config

#VOLUME ["/etc/ssh"]
#EXPOSE 3389 22 9001 993 7513 1984 1985 1022
#ENTRYPOINT ["sh","/usr/bin/docker-entrypoint.sh"]
#CMD ["supervisord"]
