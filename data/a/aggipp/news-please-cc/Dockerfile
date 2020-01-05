FROM python:3.6

# Install Open SSH and other useful networking tools for us. 
RUN apt-get update -y \
    && apt-get install -y openssh-server curl dnsutils net-tools iproute2 rsync htop screen zip vim \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /var/run/sshd
# Set up automatic login as root for ssh sessions
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Install news-please
RUN pip3 install news-please --upgrade

# Copy SSH keys for this container and set permission right
RUN mkdir /root/.ssh
COPY ssh_config/authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

# Copy script and create output dir
COPY docker.sh /
RUN chmod +x /docker.sh
RUN mkdir /npdata

# Run SSH service and the application
CMD /usr/sbin/sshd -E /var/log/ssh.log && /docker.sh
