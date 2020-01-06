FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
ENV USER root
#ENV USER_NAME ubuntu
ENV HOME /${USER}

RUN apt-get update 
RUN apt-get -y upgrade 
RUN apt-get install -y --no-install-recommends ubuntu-desktop
RUN apt-get install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xfce4-terminal
RUN apt-get install -y vnc4server openssh-server ssh-askpass
RUN apt-get install -y git vim dnsutils firefox locales sudo apt-transport-https
RUN apt-get install -y supervisor net-tools iputils-ping curl pwgen wget
#for ast running
RUN apt-get install -y libswt-gtk-3-java
#RUN apt-get install -y libtasn1-bin libglu1-mesa
#RUN apt-get install -y unity-lens-applications  gedit
#RUN apt-get install -y tightvncserver tigervnc-standalone-server tigervnc-xorg-extension tigervnc-viewer
RUN apt-get autoclean
RUN apt-get autoremove
RUN rm -rf /var/lib/apt/lists/*
#RUN dpkg --add-architecture i386
#RUN apt-get install libc6:i386 libncurses5:i386 libstdc++6:i386

#RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin yes/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#X11Forwarding yes/X11Forwarding yes/' /etc/ssh/sshd_config
RUN sed -i 's/#X11DisplayOffset 10/X11DisplayOffset 10/' /etc/ssh/sshd_config
RUN sed -i 's/#X11UseLocalhost yes/X11UseLocalhost no/' /etc/ssh/sshd_config
 
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
 
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
 
#RUN adduser ${USER} --disabled-password --shell /bin/bash
#RUN useradd -d /home/${USER} -m -p ${USER} -s /bin/bash ${USER}
#RUN adduser ${USER} sudo
#RUN echo "${USER} ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/${USER} && chmod 0440 /etc/sudoers.d/${USER}


RUN mkdir -p ${HOME}/.vnc
RUN mkdir -p ${HOME}/.config/nautilus

ADD xstartup ${HOME}/.vnc/xstartup
ADD passwd ${HOME}/.vnc/passwd
ADD entrypoint.sh /usr/local/bin/entrypoint.sh
ADD .bash_aliases ${HOME}/.bash_aliases

#RUN chown -R  ${USER}.${USER} ${HOME}

RUN chmod 644 ${HOME}/.bash_aliases
RUN chmod 600 ${HOME}/.vnc/passwd
RUN chmod 755 ${HOME}/.vnc/xstartup /usr/local/bin/entrypoint.sh

#CMD /usr/bin/vncserver :1 -geometry 1280x800 -depth 24 && tail -f /root/.vnc/*:1.log

WORKDIR ${HOME}
USER ${USER}
ENTRYPOINT /usr/local/bin/entrypoint.sh
#CMD ["/usr/sbin/sshd", "-D"]

EXPOSE 5901-5905
EXPOSE 22

