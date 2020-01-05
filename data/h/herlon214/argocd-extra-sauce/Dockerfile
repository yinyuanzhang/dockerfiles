FROM argoproj/argocd:v1.1.1

# Switch to root for the ability to perform install
USER root

# Install tools needed for your repo-server to retrieve & decrypt secrets, render manifests 
RUN apt-get update && \
    apt-get install -y \
    curl \
    unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    curl https://releases.hashicorp.com/vault/1.1.3/vault_1.1.3_linux_amd64.zip -o vault.zip && \
    unzip vault.zip && \
    rm vault.zip && \
    chmod +x vault && \
    mv ./vault /usr/local/bin/vault

# Switch back to non-root user
USER argocd
