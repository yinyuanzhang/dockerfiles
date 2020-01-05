FROM maven:3-jdk-8

# Install Python (required for AWS CLI & NodeJS)
RUN curl -sL https://deb.nodesource.com/setup_8.x|bash - \
  && apt-get update && apt-get install -y --no-install-recommends nodejs python3-pip git \
  && rm -rf /var/lib/apt/lists/*
RUN pip3 install setuptools && pip3 install awscli

