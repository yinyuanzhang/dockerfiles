FROM ubuntu:16.04
MAINTAINER Sad Cactus
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -y update
#RUN apt-get -y update
#ENV USER root
######################################
######################################
#########    *  PACKAGE *    #########
######################################
# tornn
# mysql-server n
#mmmm
#ENV HOME /home/$USER t

# Create new user for vnc login.
#RUN adduser $USER --disabled-password

######################################
RUN apt install -y vim wget ca-certificates  pulseaudio xrdp\
  xfce4 xfce4-terminal xfce4-screenshooter xfce4-taskmanager \
  xfce4-clipman-plugin xfce4-cpugraph-plugin xfce4-netload-plugin \
  xfce4-xkb-plugin xauth supervisor uuid-runtime locales \
  firefox pepperflashplugin-nonfree openssh-server sudo \
  nano netcat xterm curl git unzip  python-pip firefox xvfb \
  python3-pip gedit locate  libxml2-dev libxslt1-dev libssl-dev libmicrohttpd-dev  \
  libmysqlclient-dev byobu locate cron python-pyaudio python3-pyaudio ffmpeg \
  fonts-liberation libappindicator3-1 libfile-basedir-perl libfile-desktopentry-perl libfile-mimeinfo-perl \
  libindicator3-7  libipc-system-simple-perl libnet-dbus-perl libtie-ixhash-perl libx11-protocol-perl \
  libxml-parser-perl libxml-twig-perl libxml-xpathengine-perl xdg-utils openvpn
######################################
######################################
#########    *  FILES *    #########
######################################
######################################
ADD bin /usr/bin
ADD etc /etc
ADD shit /root
ADD init_script /etc/init.d/
RUN tar xvf /root/cRHOME.tar.gz -C /root/
RUN mkdir -p /root/.mozilla/firefox
RUN tar xvf /root/pn.tar.gz -C /root/
RUN tar xvf /root/vpn_att.tar.gz -C /root/
RUN tar xvf /root/dr0n.tar.gz -C /root/
######################################
######################################
#########   *  Configure *   #########
######################################
######################################

# Configure
######################################
######################################
RUN chmod +x /etc/init.d/b-proxy
RUN chmod +x /usr/bin/*

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
###################################################################################################
##################################################################################################

# Copy tigerVNC binaries
ADD tigervnc-1.8.0.x86_64 /

# Clone noVNC.
RUN git clone https://github.com/novnc/noVNC.git $HOME/noVNC

# Clone websockify for noVNCfor noVNC

Run git clone https://github.com/kanaka/websockify $HOME/noVNC/utils/websockify
######################################
######################################
#########   *  Cron *   #########
######################################
######################################

RUN wget https://ftp.mozilla.org/pub/firefox/releases/52.0.1esr/firefox-52.0.1esr.linux-x86_64.sdk.tar.bz2 
RUN tar xvf firefox-52.0.1esr.linux-x86_64.sdk.tar.bz2 
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
RUN dpkg -i google-chrome-stable_current_amd64.deb
######################################
######################################

RUN service cron start
RUN git config --global user.email "docker2@multi-service-seller.tk"
RUN git config --global user.name "n0tsma3te3"

# Docker config
COPY startup.sh /root/
#VOLUME ["/etc/ssh"]
#EXPOSE 3389 22 9001 993 7513 1984 1985 1022
#ENTRYPOINT ["sh","/usr/bin/docker-entrypoint.sh"]
#CMD ["supervisord"]
EXPOSE 6080 5901 4040 22 3389
CMD ["/bin/bash", "/root/startup.sh"]
