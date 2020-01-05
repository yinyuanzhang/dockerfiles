FROM ptcos/docker-dotnet-node-sdk

RUN AZ_REPO=$(lsb_release -cs) && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
      tee /etc/apt/sources.list.d/azure-cli.list && \
    curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    apt-get update -y && \
    apt-get install -y apt-transport-https azure-cli

RUN npm install -g azure-functions-core-tools

# RUN az --version
# RUN func --gpuversion

