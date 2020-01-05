FROM node:10.15.3

ENV JAVA_HOME /usr/lib/jvm/default-jvm

# First install the dependencies we actually need
RUN apt-get install curl bash git python && \
# Dependencies for building node and installing awscli
    apt-get update -y && \
    apt-cache search linux-headers- && \
    apt-get install -y \
        default-jdk \
        build-essential \
        binutils-gold \
        curl \
        g++ \
        gcc \
        gnupg \
        make \
        python-pip \
        libpython-dev && \
# Install AWS CLI
    pip install awscli && \
    cd ~ && \
# Update npm
    npm install --no-package-lock npm@6.9.0 && \
    rm -rf /usr/local/lib/node_modules && \
    mv node_modules /usr/local/lib/ && \
# Install the Heroku CLI
    npm i heroku -g && \
# Link up Java
    # ln -fs "${JAVA_HOME}/bin/"* /usr/bin/ && \
# Do cleanup
    npm cache clear --force && \
    rm -rf /var/cache/apt-get/* && \
# Test all the Utilities
    aws --version && \
    heroku --version && \
    java -version && \
    javac -version && \
    node --version && \
    npm --version

ENTRYPOINT ["/bin/bash"]
