FROM node:10

# Install pip (https://github.com/aws/aws-cli/issues/2290)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3-pip python3-setuptools \
        zip \
    && rm -rf /var/lib/apt/lists/*

        
# Install aws cli.
RUN pip3 install -U awscli

# Get docker.
RUN curl -s https://get.docker.com | bash -s

# Install docker-compose.
RUN curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose
