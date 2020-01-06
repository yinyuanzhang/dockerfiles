FROM ubuntu:latest

#### proxy environment                
#ENV http_proxy=http://host:port
#ENV https_proxy=http://host:port
RUN apt-get update  -y  && \
    apt-get dist-upgrade -y && \
    apt-get install curl gnupg gnupg2 gnupg1  vim iputils-ping -y
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl -o /etc/apt/sources.list.d/microsoft.list https://packages.microsoft.com/config/ubuntu/18.04/prod.list
RUN apt-get update -y && \
    apt-get install powershell-preview -y
RUN pwsh-preview -C install-Module -Name VMware.PowerCLI -force
RUN pwsh-preview -C set-powercliconfiguration -InvalidcertificateAction:ignore -scope:user -Confirm':$false'


#### importing modules 
### ading new profile file
#RUN pwsh-preview -C New-Item –Path '$Profile' –Type File –Force
### Copy module into newly created profile file
#COPY urmodule-script.ps1 /root/.config/powershell/Microsoft.PowerShell_profile.ps1
### copy scripts if u have any
#COPY urposwershell-Powercli_scripts.ps1 /


### it's depends on where ur remote scripts are executing removing proxy or not 

#ENV http_proxy=
#ENV https_proxy=
