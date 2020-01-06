FROM ubuntu:trusty
MAINTAINER Karl Jahn <kajahno@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to UK
RUN sed -i "s/http:\/\/archive./http:\/\/uk.archive./g" /etc/apt/sources.list

# Install Python runtime
RUN apt-get update && \
    apt-get install -qy \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv \
    libpython2.7 \
    python-mysqldb

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.bash /usr/local/bin/entrypoint.bash
RUN chmod +x /usr/local/bin/entrypoint.bash
ENTRYPOINT [ "entrypoint.bash" ]

LABEL application="todobackend"
