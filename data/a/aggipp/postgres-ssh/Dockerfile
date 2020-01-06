FROM postgres:11

# Install Open SSH and other useful networking tools for us. 
RUN apt-get update -y \
    && apt-get install -y openssh-server curl net-tools iproute2 screen zip vim rsync supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /var/run/sshd
# Set up automatic login as root for ssh sessions
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

# Copy SSH keys for this container and set permission right
RUN mkdir /root/.ssh
COPY ssh_config/authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

# Configure supervisord
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Run supervisor with sub-processes
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
