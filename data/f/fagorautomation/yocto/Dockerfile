
# Pull base image.
FROM fagorautomation/ubuntu-base:v1.01

USER root

RUN apt-get update

# Ubuntu Yocto dependencies (Mega Manual):
# Essentials
RUN apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib \
build-essential chrpath socat cpio python python3 python3-pip python3-pexpect \
xz-utils debianutils iputils-ping file

# Graphical and Eclipse Plugin Extras
RUN apt-get install -y libsdl1.2-dev xterm

# Documentation
RUN apt-get install -y make xsltproc docbook-utils fop dblatex xmlto

# OpenEmbedded Self-Test
RUN apt-get install -y python-git

# kernel compilation rpi needs this
RUN apt-get install -y bc libncursesw5-dev

# Kernel CONFIG_UNWINDER_ORC need this
RUN apt-get install -y libelf-dev

USER developer

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]
