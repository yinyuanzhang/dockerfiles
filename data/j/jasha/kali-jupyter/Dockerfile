FROM kalilinux/kali-linux-docker
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y metasploit-framework
RUN apt install -y jupyter-notebook
RUN apt install -y python3-pip python3-ipython python3-ipykernel
RUN pip3 install bash_kernel
RUN python3 -m bash_kernel.install
RUN apt install -y openssh-server vim
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo "Port 2222" >> /etc/ssh/sshd_config
RUN echo "root:easytoguess"|chpasswd
RUN pip3 install jupyter_contrib_nbextensions
RUN jupyter nbextensions_configurator enable --user
RUN apt install -y openvpn
RUN apt-get -y update && apt-get -y upgrade && \
    apt-get install -y kali-linux-full --fix-missing && \
    apt-get install -y \
    software-properties-common \
    bash-completion git colordiff colortail unzip vim tmux zsh curl telnet strace ltrace tmate && \
    apt-get autoremove -y && \
    apt-get clean
RUN mkdir /data
RUN apt-get update && \
    apt-get install -y --fix-missing git python tightvncserver x11vnc gnome && \
    apt-get autoremove -y && \
    apt-get clean && \
    git clone --depth 1 https://github.com/novnc/noVNC.git /root/noVNC && \
    git clone --depth 1 https://github.com/novnc/websockify.git /root/noVNC/utils/websockify 
ADD start.sh /
ADD .vnc /root/.vnc
ADD .Xauthority /root/.Xauthority
RUN chmod +x /start.sh
RUN apt install -y vnc4server tigervnc-common tigervnc-standalone-server
RUN echo "easytoguess" | vncpasswd -f > /root/.vnc/passwd
ADD .jupyter /root/.jupyter
RUN echo "PermitEmptyPasswords yes" >> /etc/ssh/sshd_config
RUN echo "root:toor"|chpasswd

EXPOSE 5901 6080 2222 8888
ENV USER root

CMD [ "/start.sh" ]