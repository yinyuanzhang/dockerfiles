FROM microsoft/windowsservercore

MAINTAINER Thiago Gonzaga <thiago.gonzaga@aurea.com>

RUN powershell Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force

RUN powershell Install-Module -Name 7Zip4Powershell -Force

RUN powershell New-Item -Type Directory C:\\blackbox_exporter

RUN powershell Invoke-WebRequest -Uri https://github.com/prometheus/blackbox_exporter/releases/download/v0.4.0/blackbox_exporter-0.4.0.windows-amd64.tar.gz -OutFile C:\\blackbox_exporter\\blackbox_exporter-0.4.0.windows-amd64.tar.gz

RUN powershell Expand-7zip C:\\blackbox_exporter\\blackbox_exporter-0.4.0.windows-amd64.tar.gz C:\\blackbox_exporter

RUN powershell Expand-7zip C:\\blackbox_exporter\\blackbox_exporter-0.4.0.windows-amd64.tar \"C:\\Program Files\"

WORKDIR C:\\Program\ Files\\blackbox_exporter-0.4.0.windows-amd64

ENTRYPOINT ["blackbox_exporter.exe"]

CMD ["-config.file=blackbox.yml"]

EXPOSE 9115