FROM microsoft/windowsservercore

MAINTAINER Thiago Gonzaga <thiago.gonzaga@aurea.com>

RUN powershell Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force

RUN powershell Install-Module -Name 7Zip4Powershell -Force

RUN powershell New-Item -Type Directory C:\\pushgateway

RUN powershell Invoke-WebRequest -Uri https://github.com/prometheus/pushgateway/releases/download/v0.3.1/pushgateway-0.3.1.windows-amd64.tar.gz -OutFile C:\\pushgateway\\pushgateway-0.3.1.windows-amd64.tar.gz

RUN powershell Expand-7zip C:\\pushgateway\\pushgateway-0.3.1.windows-amd64.tar.gz C:\\pushgateway

RUN powershell Expand-7zip C:\\pushgateway\\pushgateway-0.3.1.windows-amd64.tar \"C:\\Program Files\"

WORKDIR C:\\Program\ Files\\pushgateway-0.3.1.windows-amd64

ENTRYPOINT ["pushgateway.exe"]

EXPOSE 9091