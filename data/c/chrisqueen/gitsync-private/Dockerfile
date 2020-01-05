FROM openweb/git-sync:latest

# Add the keys and config
COPY keys/id_rsa /root/.ssh/id_rsa
COPY keys/ssh_config /etc/ssh/ssh_config

# Authorize SSH Host and chmod private key
RUN mkdir -p ~/.ssh && \
    chmod 0700 ~/.ssh && \
    touch /root/.ssh/known_hosts && \
    ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts && \
    ssh-keyscan -t rsa bitbucket.org >> ~/.ssh/known_hosts && \
    chmod 600 ~/.ssh/id_rsa

