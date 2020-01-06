# Java 8 as a base image
FROM openjdk:8-jdk-slim

# For Maven
RUN mkdir -p /usr/share/man/man1

# Install everything the server needs.
RUN apt-get update \
 && apt-get install -y supervisor openssh-server wget\
    less\
    vim\
    nano\
    curl\
    screen\
    build-essential\
    git\
    maven\
 && apt-get clean

# Copy SSH keys allowed for this container.
RUN mkdir /root/.ssh & mkdir -p /run/sshd
COPY ssh_key.pub /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

# Start up supervisor to run any necessary processes on container startup.
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
