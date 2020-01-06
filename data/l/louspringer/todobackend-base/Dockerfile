FROM ubuntu:bionic
MAINTAINER Lou Springer <lou@louspringer.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to NZ
# RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

# Install Python runtime
# modified python python-virtualenv libpython2.7 python-mysqldb
RUN apt-get update && \
    apt-get install -qy \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python3-pip libpython3.6 && \
    pip3 install virtualenv PyMySQL

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
RUN virtualenv -p python3 /appenv && \
    . /appenv/bin/activate && \
    pip3 install pip --upgrade

EXPOSE 8888

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

LABEL application=todobackend