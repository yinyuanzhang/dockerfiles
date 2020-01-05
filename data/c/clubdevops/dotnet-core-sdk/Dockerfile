FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env

LABEL maintainer="alllexandr@g,ail.com"
LABEL description="DotNet core sdk extended image with powershall and so on"

RUN apt-get update
RUN apt-get install -y curl gnupg apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-debian-stretch-prod stretch main" > /etc/apt/sources.list.d/microsoft.list'
RUN apt-get update
RUN apt-get install -y powershell
RUN ln -s /usr/bin/pwsh /usr/bin/PowerShell


