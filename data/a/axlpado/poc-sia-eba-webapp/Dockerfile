#
# Java (Oracle Java 7 JDK) + SSH Dockerfile
#
# Version               0.0.0

# Pull base image.
FROM dockerfile/java:oracle-java7

# Define maintainer
MAINTAINER axlpado

# Install SSH
RUN apt-get update && apt-get install -y openssh-server

# Configure SSH
RUN mkdir /var/run/sshd
RUN echo 'root:root' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN apt-get install -y --force-yes unzip
RUN apt-get install git

RUN cd /home && wget http://downloads.typesafe.com/play/2.2.1/play-2.2.1.zip && unzip play-2.2.1.zip && rm /home/play-2.2.1.zip

ENV PLAYPATH /home/play-2.2.1
ENV PATH $PLAYPATH:$PATH

# Expose SSH
EXPOSE 22
EXPOSE 9000

RUN mkdir /home/play_apps
RUN cd /home/play_apps
RUN mkdir poc_sia_eba
WORKDIR /home/play_apps/poc_sia_eba/target/universal/CM-2.1/bin

# Start play
CMD ["cm", "-D"]