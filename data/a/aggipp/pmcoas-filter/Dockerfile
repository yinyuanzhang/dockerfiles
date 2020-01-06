# A web app to recognize whether a text was machine-paraphrased
# https://cloud.docker.com/repository/docker/tfoltynek/original-or-spun
FROM ubuntu:18.04
LABEL maintainer="Vincent Stange, vincent.stange@uni-konstanz.de"

# Our SSH Client configuration:
# Install Open SSH and other useful networking tools.
RUN apt-get update -y \
    && apt-get install -y openssh-server curl dnsutils net-tools iputils-ping iproute2 jq nano htop \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /var/run/sshd
# Set up automatic login as root for ssh sessions and prepare ssh folder
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config \
    && sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \
    && mkdir /root/.ssh
# Copy SSH keys for this container
COPY ssh_config/authorized_keys /root/.ssh/authorized_keys
# SSH daemon update
CMD /usr/sbin/sshd -D

# Our custom software we want installed:
# We want python and pip
RUN apt-get update -y \
    && apt-get install -y python-pip python-dev build-essential
# Install tmux for multi-session window
RUN apt-get update -y \
	&& apt-get install -y tmux

# Copy our example application into the container
# This way, the application is persistent
COPY src /app
RUN pip install -r /app/requirements.txt
