FROM atlassian/default-image:2

# Setup dependencies
RUN mkdir -p ~/bin && \
    cd ~/bin && \
    export PATH="$PATH:/root/bin" && \
    add-apt-repository ppa:ondrej/php -y && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update -y && \
    apt-get install -y unzip python-pip git php5.6 apt-transport-https php5.6-xml && \
# Get Atlassian SDK
    sh -c 'echo "deb https://packages.atlassian.com/atlassian-sdk-deb stable contrib" >>/etc/apt/sources.list' && \
    wget https://packages.atlassian.com/api/gpg/key/public && \
    apt-key add public && \
    apt-get update && \
    apt-get install atlassian-plugin-sdk=8.0.7 && \
# Install AWS CLI
    pip install awscli && \
# Update npm
    cd ~ && \
    npm install npm@latest && \
    rm -rf /usr/local/lib/node_modules && \
    mv node_modules /usr/local/lib/ && \
# Do cleanup
    npm cache clear --force && \
    rm -rf /var/cache/apt-get/* && \
# Test all the Utilities
    aws --version && \
    java -version && \
    npm --version && \
    atlas-version

ENTRYPOINT ["/bin/bash"]
