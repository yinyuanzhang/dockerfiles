FROM mcr.microsoft.com/dotnet/core/sdk:3.1
WORKDIR /app

RUN apt-get update
RUN apt-get install -y openjdk-11-jre
RUN apt-get install -y gpg
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o microsoft.asc.gpg
RUN mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/
RUN wget -q https://packages.microsoft.com/config/ubuntu/19.04/prod.list
RUN mv prod.list /etc/apt/sources.list.d/microsoft-prod.list
RUN chown root:root /etc/apt/trusted.gpg.d/microsoft.asc.gpg
RUN chown root:root /etc/apt/sources.list.d/microsoft-prod.list
RUN apt-get install -y apt-transport-https
RUN apt-get update
RUN apt-get install dotnet-sdk-2.1 -y
