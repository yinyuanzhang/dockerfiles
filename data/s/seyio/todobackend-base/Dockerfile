    
FROM ubuntu:latest
MAINTAINER Justin Menga <justin.menga@gmail.com>

# Prevent dpkg errors
ENV TERM=xterm-256color

# Set mirrors to NZ
# RUN sed -i "s/http:\/\/archive./http:\/\/nz.archive./g" /etc/apt/sources.list

# Install Python runtime
RUN apt-get update \
  && apt-get install -y --no-install-recommends python3-pip python3-dev python3-virtualenv build-essential libpcre3 libpcre3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# Create virtual environment
# Upgrade PIP in virtual environment to latest version
RUN python3 -m virtualenv --python=/usr/bin/python3 /appenv && \
    . /appenv/bin/activate && \
    pip3 install pip --upgrade

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]

LABEL application=todobackend
