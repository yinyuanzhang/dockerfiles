FROM ubuntu:18.04
RUN apt-get update && \
    apt-get install -y curl software-properties-common && \
    (curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash) && \
    apt-get update && \
    apt-get install -y git-lfs ant unzip python-dev jq gettext-base webp && \
    curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o /tmp/awscli-bundle.zip && \
    cd /tmp && \
    unzip awscli-bundle.zip && \
    ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws && \
    rm -rf {/tmp/*,/var/lib/apt/lists/*}
RUN (curl -sL https://deb.nodesource.com/setup_9.x | bash) && \
    apt-get update && \
    apt-get install -y nodejs && \
    npm install -g s3-website && \
    rm -rf /var/lib/apt/lists/*
RUN curl -L https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-3.3.0.1492-linux.zip -o /opt/sonar-scanner.zip && \
    cd /opt && \
    unzip sonar-scanner.zip && \
    ln -s sonar-scanner-3.3.0.1492-linux sonar-scanner && \
    rm sonar-scanner.zip
