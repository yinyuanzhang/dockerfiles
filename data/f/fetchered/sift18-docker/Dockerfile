FROM ubuntu:bionic 
ENV container docker 
ENV PATH "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

RUN apt update && \
export DEBIAN_FRONTEND=noninteractive && \
apt install -y \
software-properties-common \
wget \
gnupg && \
wget -O - http://repo.saltstack.com/apt/ubuntu/18.04/amd64/2018.3/SALTSTACK-GPG-KEY.pub | apt-key add - && \
echo "deb http://repo.saltstack.com/apt/ubuntu/18.04/amd64/2018.3 bionic main" | tee /etc/apt/sources.list.d/saltstack.list &&\
add-apt-repository ppa:malteworld/ppa && \
apt-get update &&\
apt-get install -y \
salt-minion \
ant \
build-essential \
curl \
default-jdk-headless \
fuse \
gcc \
init \
libbcprov-java \
libcommons-lang3-java \
less \
make \
nano \
p7zip \
pdftk \
sudo \
unzip \
zip && \
apt clean && \
apt autoremove -y && \
curl -Lo /usr/local/bin/sift https://github.com/sans-dfir/sift-cli/releases/download/v1.7.1/sift-cli-linux && \
chmod +x /usr/local/bin/sift

RUN groupadd -r forensics && \
useradd -r -g forensics -d /home/forensics -s /sbin/nologin -c "SIFT User" forensics && \
mkdir /home/forensics && \
chown -R forensics:forensics /home/forensics && \
usermod -a -G sudo forensics
RUN sudo sift install --pre-release --mode=packages-only --user=forensics
