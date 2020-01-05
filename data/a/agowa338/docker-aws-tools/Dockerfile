FROM microsoft/powershell:latest

RUN pwsh -OutputFormat Text -NonInteractive -NoProfile -NoLogo -Command '$ProgressPreference="SilentlyContinue";Install-Module -Name AWSPowerShell.NetCore -AllowClobber -Force'

CMD ["pwsh"]
