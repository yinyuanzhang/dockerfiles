# taken from https://gist.github.com/chssch/22e4b9214205221708f298ae7649d354
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

# Copy SSH keys for this container and set permission right
RUN mkdir /root/.ssh
COPY ssh_config/authorized_keys /root/.ssh/authorized_keys
RUN chmod 600 /root/.ssh/authorized_keys

RUN mkdir /prodigy
RUN mkdir /prodigy/home
RUN mkdir /prodigy/home/session1
RUN mkdir /prodigy/home/session2
RUN mkdir /prodigy/home/session3

WORKDIR /prodigy

COPY annofiles/ /prodigy/annofiles/
COPY newstsarecipe.py /prodigy
COPY manual.html /prodigy

EXPOSE 8081
EXPOSE 8082
EXPOSE 8083

# Copy script and create output dir
COPY docker.sh /
RUN chmod +x /docker.sh

# Run SSH service and the application
CMD /usr/sbin/sshd -E /var/log/ssh.log && /docker.sh
