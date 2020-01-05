FROM ubuntu:16.04

RUN apt-get update && apt-get install -y wget apt-transport-https && \
        sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-release/ xenial main" > /etc/apt/sources.list.d/dotnetdev.list' && \
        apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893 && \
        apt-get update && apt-get install -y dotnet-dev-1.0.0-preview2-003131 && \
        wget https://github.com/Microsoft/vsts-agent/releases/download/v2.107.1/vsts-agent-ubuntu.16.04-x64-2.107.1.tar.gz && \
        tar xzf vsts-agent-ubuntu.16.04-x64-2.107.1.tar.gz

COPY entrypoint.sh /

RUN chmod +x /entrypoint.sh

CMD [ "/entrypoint.sh" ]
