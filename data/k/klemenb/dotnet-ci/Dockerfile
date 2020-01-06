FROM microsoft/dotnet:2.2-sdk

LABEL maintainer="klemen.bratec@gmail.com"

# Install utilities and prerequisites
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --no-install-recommends curl vim nano bzip2 wget unzip sqlite apt-utils apt-transport-https gettext && \
    apt-get install -y --no-install-recommends git subversion mercurial ssh && \
    apt-get install -y --no-install-recommends python3 python3-pip python3-setuptools && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip3 install ansible requests google-auth

# Install Node.js along with gulp and grunt
RUN VERSION=node_11.x && \
    curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add - && \
    echo "deb https://deb.nodesource.com/$VERSION stretch main" | tee /etc/apt/sources.list.d/nodesource.list && \
    echo "deb-src https://deb.nodesource.com/$VERSION stretch main" | tee -a /etc/apt/sources.list.d/nodesource.list && \
    DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --no-install-recommends nodejs && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    npm install -g npm@latest gulp grunt
