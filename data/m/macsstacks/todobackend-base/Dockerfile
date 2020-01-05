FROM ubuntu:trusty
MAINTAINER Callum MacDonald <TheMacStack@pm.me>
LABEL application=todobackend

#prevent dpkg errors
ENV TERM=xterm-256color

# Install Python runtime
RUN apt-get update && \
    apt-get install -y \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv libpython2.7 python-mysqldb

# Create virtual environment
# Upgrade PIP in virtual env to latest version
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade    

# Add entrypoint script
ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]