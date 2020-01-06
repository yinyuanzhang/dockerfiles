# Start from Ubuntu latest
FROM ubuntu:18.04

# Update apt
RUN apt-get update && yes|apt-get upgrade

RUN apt-get install -y wget sudo vim
# Add user ubuntu with no password, add to sudo group
RUN adduser --disabled-password --gecos '' ubuntu
RUN adduser ubuntu sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
USER ubuntu
WORKDIR /home/ubuntu/
RUN chmod a+rwx /home/ubuntu/

