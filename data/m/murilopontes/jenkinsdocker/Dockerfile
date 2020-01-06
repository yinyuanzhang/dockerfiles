FROM jenkins/jenkins:lts

#
COPY plugins.txt /
RUN /usr/local/bin/install-plugins.sh < /plugins.txt

#
USER root

RUN curl -fsSL https://get.docker.com -o get-docker.sh &&  sh get-docker.sh

RUN curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose


# Yocto required 
RUN apt-get update && DEBIAN_FRONTEND=noninteractive  apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib \
build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
xz-utils debianutils iputils-ping libsdl1.2-dev xterm

# Yocto required
RUN apt-get update && DEBIAN_FRONTEND=noninteractive  apt-get install -y autoconf libtool libglib2.0-dev libarchive-dev python-git \
sed cvs subversion coreutils texi2html docbook-utils python-pysqlite2 \
help2man make gcc g++ desktop-file-utils libgl1-mesa-dev libglu1-mesa-dev \
mercurial automake groff curl lzop asciidoc u-boot-tools dos2unix mtd-utils pv \
libncurses5 libncurses5-dev libncursesw5-dev libelf-dev zlib1g-dev

# Cmake and ninja
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y cmake ninja-build

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y pxz


###### LOCALES
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

###########


RUN usermod -a -G docker jenkins
RUN usermod -a -G root jenkins
RUN usermod -a -G disk jenkins
#RUN chown -v root:jenkins /var/run/docker.sock

#USER jenkins
