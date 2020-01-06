# Node.js Dockerfile
# Pull base image.
FROM antik486/centos71

# Prepare enviroment for Node.js installation
RUN yum -y update && \
    yum install -y wget && \
    yum groupinstall -y "Development Tools" && \
    yum clean all && \
    rm -rf /var/tmp/*

# Install Node.js
RUN \
    cd /tmp && \
    wget http://nodejs.org/dist/node-latest.tar.gz && \
    tar xvzf node-latest.tar.gz && \
    rm -f node-latest.tar.gz && \
    cd node-v* && \
    ./configure && \
    CXX="g++ -Wno-unused-local-typedefs" make && \
    CXX="g++ -Wno-unused-local-typedefs" make install && \
    cd /tmp && \
    rm -rf /tmp/node-v* && \
    npm install -g npm && \
    printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]
