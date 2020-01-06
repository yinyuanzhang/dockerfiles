# escape=`
FROM microsoft/powershell:latest

RUN apt-get update && apt-get install -y curl jq vim-tiny && rm -f /var/cache/apt/archives/partial/*

SHELL ["/usr/bin/pwsh", "-c"]
RUN $ErrorActionPreference='Stop'; `
    Start-Transcript -path /Dockerfile.log -append -IncludeInvocationHeader ; `
    $PSVersionTable | Write-Output ; `
    Install-Module -Name AWSPowerShell.NetCore -AllowClobber -Force ; `
    New-Item /root/.config/powershell/ -Type Directory -Force ; `
    Stop-Transcript ;

# Copy in my custom powershell module files that are "imported" in the profile bellow
#ADD ./ /mnt/MyCustomPSM1Dir

# Use pwsh profile to initialize my custom powershell module
ADD ./profile.ps1 /root/.config/powershell/Microsoft.PowerShell_profile.ps1

# Default commands to pwsh
ENTRYPOINT ["pwsh"]
