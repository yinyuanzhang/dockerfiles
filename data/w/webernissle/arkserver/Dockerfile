#
# ARK server with ARK management tools
#
# inspired by https://github.com/TuRz4m/Ark-docker
#

# docker build -t arkserver:latest .
# docker run -d --rm -p 8085:8080 --name arkserver arkserver
# docker run -t -i --rm -p 8085:8080 --name arkserver arkserver
# docker run -t -i --rm -p 8085:8080 --entrypoint /bin/bash --name arkserver arkserver
# docker exec -t -i arkserver /bin/bsh
# docker logs arkserver
# docker stop arkserver
FROM ubuntu:18.04

MAINTAINER Martin Weber Nisslé

# Var for first config
# Server Name
ENV SESSIONNAME "Ark Docker"
# Map name
ENV SERVERMAP "TheIsland"
# Server password
ENV SERVERPASSWORD ""
# Admin password
ENV ADMINPASSWORD "adminpassword"
# Nb Players
ENV NBPLAYERS 70
# If the server is updating when start with docker start
ENV UPDATEONSTART 1
# if the server is backup when start with docker start
ENV BACKUPONSTART 1
#  Tag on github for ark server tools
ENV GIT_TAG v1.6.02
# Server PORT (you can't remap with docker, it doesn't work)
ENV SERVERPORT 27015
# Steam port (you can't remap with docker, it doesn't work)
ENV STEAMPORT 7778
# if the server should backup after stopping
ENV BACKUPONSTOP 0
# If the server warn the players before stopping
ENV WARNONSTOP 0
# UID of the user steam
ENV UID 1000
# GID of the user steam
ENV GID 1000

# Install dependencies
RUN apt-get update && \
    apt-get upgrade -y  && \
    apt-get install -y curl lsof git

RUN dpkg --add-architecture i386 && \
 apt-get install -y lib32gcc1 && \
 apt-get update
RUN echo steam steam/question select "I AGREE" | debconf-set-selections
RUN echo steam steam/license note '' | debconf-set-selections

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y steamcmd

# Run commands as the steam user
RUN adduser \
	--disabled-login \
	--shell /bin/bash \
	--gecos "" \
	steam
# Add to sudo group
RUN usermod -a -G sudo steam
# Enable passwordless sudo for users under the "sudo" group
COPY steamsudoer /etc/sudoers.d/steamsudoer
#RUN sed -i.bkp -e \
#	's/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/%sudo ALL=NOPASSWD:ALL/g' /etc/sudoers \
#	/etc/sudoers

# Copy & rights to folders
COPY run.sh /home/steam/run.sh
COPY user.sh /home/steam/user.sh
COPY crontab /home/steam/crontab
COPY arkmanager-user.cfg /home/steam/arkmanager.cfg

RUN touch /root/.bash_profile
RUN chmod 777 /home/steam/run.sh
RUN chmod 777 /home/steam/user.sh
RUN mkdir  /ark


# We use the git method, because api github has a limit ;)
RUN  git clone https://github.com/FezVrasta/ark-server-tools.git /home/steam/ark-server-tools
WORKDIR /home/steam/ark-server-tools/
RUN  git checkout $GIT_TAG
# Install
WORKDIR /home/steam/ark-server-tools/tools
RUN chmod +x install.sh
RUN ./install.sh steam

# Allow crontab to call arkmanager
RUN ln -s /usr/local/bin/arkmanager /usr/bin/arkmanager

# Define default config file in /etc/arkmanager
COPY arkmanager-system.cfg /etc/arkmanager/arkmanager.cfg

# Define default config file in /etc/arkmanager
COPY instance.cfg /etc/arkmanager/instances/main.cfg

RUN chown steam -R /ark && chmod 755 -R /ark

#USER steam

# download steamcmd
RUN mkdir /home/steam/steamcmd &&\
	cd /home/steam/steamcmd &&\
	curl http://media.steampowered.com/installer/steamcmd_linux.tar.gz | tar -vxz


# First run is on anonymous to download the app
# We can't download from docker hub anymore -_-
#RUN /home/steam/steamcmd/steamcmd.sh +login anonymous +quit

EXPOSE ${STEAMPORT} 32330 ${SERVERPORT}
# Add UDP
EXPOSE ${STEAMPORT}/udp ${SERVERPORT}/udp

VOLUME  /ark

# Change the working directory to /arkd
WORKDIR /ark

# Update game launch the game.
ENTRYPOINT ["/home/steam/user.sh"]