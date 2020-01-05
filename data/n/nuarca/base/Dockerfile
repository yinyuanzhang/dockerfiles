FROM microsoft/mssql-server-linux
MAINTAINER Shafqat Ahmed

RUN   mkdir /app  && cd /app && \
      apt update && \
      apt install -y  build-essential libssl-dev nano wget git curl jq realpath unzip && \
      cd /tmp && \      
      wget https://deb.nodesource.com/setup_6.x && \ 
      chmod +x setup_6.x && \
      ./setup_6.x && \
      apt install nodejs -y && \
      npm install forever -g
RUN   npm install -g yaml-cli 
#RUN   apt install -y realpath
#RUN   echo $TERM
#RUN   cd /tmp && wget https://packages.microsoft.com/ubuntu/16.04/prod/pool/main/m/msodbcsql/msodbcsql_13.1.6.0-1_amd64.deb &&  ACCEPT_EULA=Y dpkg -i msodbcsql_13.1.6.0-1_amd64.deb
#RUN   cd /tmp && wget https://packages.microsoft.com/ubuntu/16.04/prod/pool/main/m/mssql-tools/mssql-tools_14.0.5.0-1_amd64.deb && ACCEPT_EULA=Y dpkg -i mssql-tools_14.0.5.0-1_amd64.deb
#RUN   apt-get install -y unixodbc-dev libodb-2.4
#RUN   mkdir -p /opt/mssql-tools/share/resources/en_US
#RUN   curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add - && \
#      curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list && \
#      apt update && \      
#RUN   apt install -y mssql-tools unixodbc-dev  nano 
#RUN   cd /tmp && wget https://github.com/PowerShell/PowerShell/releases/download/v6.0.0-beta.7/powershell_6.0.0-beta.7-1ubuntu1.16.04.1_amd64.deb && \
#      dpkg -i powershell_6.0.0-beta.7-1ubuntu1.16.04.1_amd64.deb && \
#      apt-get install -f && \
