FROM debian:unstable 

# Setup enviroment variables
ENV DEBIAN_FRONTEND noninteractive

#Update the package manager and upgrade the system
RUN apt-get update && \
apt-get dist-upgrade -y && \ 
apt-get install -y expect blackbox firefox sudo tightvncserver xorg --no-install-recommends

# Define mountable directories.
VOLUME ["/data"]

# Define working directory.
WORKDIR /data

# Create user (add script and execute)
ADD create-user.sh /usr/local/etc/create-user.sh
RUN chmod 700 /usr/local/etc/create-user.sh && sleep 1 &&  /usr/local/etc/create-user.sh

# Setup sudo
RUN echo "user ALL=NOPASSWD: ALL" >> /etc/sudoers &&\
echo "" >> /etc/sudoers


# Add expect script (to set password)
ADD start-vnc-expect-script.sh /usr/local/etc/start-vnc-expect-script.sh
RUN chmod 755 /usr/local/etc/start-vnc-expect-script.sh

# Add script to spawn desktop
ADD spawn-desktop.sh /usr/local/etc/spawn-desktop.sh
RUN chmod u+x /usr/local/etc/spawn-desktop.sh

# Add documentation
ADD welcome.html /usr/local/etc/welcome.html

# Define default command.
CMD /usr/local/etc/spawn-desktop.sh;bash

# Expose ports.
EXPOSE 5901
