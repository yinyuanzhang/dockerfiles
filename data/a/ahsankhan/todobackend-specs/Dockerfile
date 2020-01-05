FROM ubuntu:trusty
LABEL maintainer="Ahsanuzzaman Khan <ahsan.khan434@gmail.com>"

# Prevent dpkg errors
ENV TERM=xterm-256color

# Install node.js
RUN apt-get update && \
    apt-get install curl -y && \
    curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \
    apt-get install -y nodejs

COPY . /app
WORKDIR /app

# Install application dependencies
RUN npm install -g mocha@5.2.0 && \
    npm install

# OUTPUT: Test reports are output here
VOLUME [ "/reports" ]

# Set mocha test runner as entrypoint
ENTRYPOINT [ "mocha" ]