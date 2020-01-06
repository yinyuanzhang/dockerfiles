FROM debian:7.11
# last build: 24-09-2018 14:19:30

RUN apt-get update && apt-get -y upgrade && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get autoclean && apt-get clean
RUN apt-get install -y wget cron netcat-traditional nano 

# the following list of images is taken from the golden_image base - cookbook. The docker iamge is meant to resemble the actual VM
# as closely as possible.
RUN apt-get install -y bc bsd-mailx ca-certificates curl dbus debian-goodies di dnsutils dos2unix dstat figlet finger gnupg htop ifstat iftop inotify-tools ipcalc less lsb-release lsof lynx mc mlocate moreutils multitail mutt ncdu net-tools ntp ntpdate openssh-server p7zip parted perl pktstat psmisc recode rsync screen slurm sudo sysstat tcpdump tcpflow tcsh telnet tmux tree unzip vim vim-runtime w3m xfsprogs zip

RUN cd /tmp \
    && wget https://packages.chef.io/files/stable/chef/12.21.26/debian/7/chef_12.21.26-1_amd64.deb \ 
    && dpkg -i chef_12.21.26-1_amd64.deb \ 
    && apt-get autoremove \
    && rm -r "/tmp/"*
