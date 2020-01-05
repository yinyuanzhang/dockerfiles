FROM docker:18.06

# Add python pip and bash
RUN apk add --no-cache py-pip bash

# Install docker-compose via pip
RUN pip install --no-cache-dir docker-compose

# Install curl, git and etc.
RUN apk add --no-cache curl git openssl wget openssh nano
