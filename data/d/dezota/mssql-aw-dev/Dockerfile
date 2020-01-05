FROM ubuntu:16.04
MAINTAINER Brian Holman <bholman@dezota.com>

ENV DEBIAN_FRONTEND=noninteractive

# Set default timezone
RUN ln -fs /usr/share/zoneinfo/America/Denver /etc/localtime

# Ensure everything is up-to-date
RUN apt-get update --fix-missing && \
    apt-get -y upgrade

# Install System Packages
RUN apt-get install -y wget software-properties-common python-software-properties apt-transport-https sudo locales

# Generate Locale
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen 

# Configure the MSFT repo and install SQL Server, Full Text Search, and SSIS
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list)" && \
    apt-get update && \
    apt-get install -y mssql-server mssql-server-fts mssql-server-is

RUN wget -O /usr/bin/systemctl "https://raw.githubusercontent.com/gdraheim/docker-systemctl-replacement/master/files/docker/systemctl.py" && \
    chmod +x /usr/bin/systemctl

ENV SA_PASSWORD="Chang3M3R1ghtN0w" ACCEPT_EULA=Y

RUN apt-get install curl && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee /etc/apt/sources.list.d/msprod.list && \
    apt-get update && \
    apt-get -y install mssql-tools unixodbc-dev && \
    echo "export PATH=\"$PATH:/opt/mssql-tools/bin:/opt/ssis/bin\"" >> ~/.bashrc

# Setup Developor Edition License    
RUN echo "2" | /opt/mssql/bin/mssql-conf setup && \
    echo "2" | /opt/ssis/bin/ssis-conf setup

# Setup SQL Agent
RUN /opt/mssql/bin/mssql-conf set sqlagent.enabled true

COPY run.sh /run.sh

RUN chmod +x /run.sh && \
    mkdir /backups

# Install AdventureWorks demo database    
RUN wget -O /backups/AdventureWorksDW2016_EXT.bak "https://github.com/Microsoft/sql-server-samples/releases/download/adventureworks/AdventureWorksDW2016_EXT.bak"
#COPY AdventureWorksDW2016_EXT.bak /backups/AdventureWorksDW2016_EXT.bak

RUN systemctl start mssql-server && \
    sleep 30 && \
    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'Chang3M3R1ghtN0w' -Q "USE [master]; RESTORE DATABASE [AdventureWorksDW2016_EXT] FROM  DISK = N'/backups/AdventureWorksDW2016_EXT.bak' WITH  FILE = 1,  MOVE N'AdventureWorksDW2016_EXT_Data' TO N'/var/opt/mssql/data/AdventureWorksDW2016_EXT_Data.mdf',  MOVE N'AdventureWorksDW2016_EXT_Log' TO N'/var/opt/mssql/data/AdventureWorksDW2016_EXT_Log.ldf',  NOUNLOAD,  STATS = 5;" && \
    rm -f /backups/AdventureWorksDW2016_EXT.bak

# Install who_is_active for SQL Operations Studio plugin
#RUN systemctl start mssql-server && \
#    apt-get -y install unzip && \
#    wget http://whoisactive.com/downloads/who_is_active_v11_30.zip && \
#    unzip who_is_active_v11_30.zip && \
#    /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 'Chang3M3R1ghtN0w' -i who_is_active_v11_30.sql

CMD ["/run.sh"]
