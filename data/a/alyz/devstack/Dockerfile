#
# Dockerfile for alyz/devstack
#

# Pull base image.
FROM alyz/devenv:20170710

# Install uwsgi nginx sshd
RUN apt-get install -y uwsgi  \
    && apt-get install -y uwsgi-plugin-python uwsgi-plugin-python3 \
    && apt-get install -y nginx \
    && apt-get install -y openssh-server

RUN mkdir -p /var/run/sshd

expose 80
expose 22
