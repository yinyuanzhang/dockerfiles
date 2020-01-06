FROM microsoft/mssql-server-linux:latest

MAINTAINER RELENG@liaisonedu.com

LABEL description="microsoft/mssql-server-linux with mssql-tools already insalled"

ENV ACCEPT_EULA=Y

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# sql tools setup; 
RUN \
echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc && \
locale-gen en_US.UTF-8 && \
update-locale && \
apt-get update && \
apt-get install -y python sudo curl apt-transport-https && \
curl --fail --silent --show-error --location https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor | tee /usr/share/keyrings/microsoft-archive-keyring.gpg > /dev/null && \
curl --fail --silent --show-error --location https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list | sed "s@arch=amd64@arch=amd64 signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg@" | tee /etc/apt/sources.list.d/mssql-server.list > /dev/null && \
apt-get update && \
apt-get install -y mssql-tools mssql-server-fts tzdata

## Set timezone
#
ENV TZ=America/New_York
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

EXPOSE 1433
