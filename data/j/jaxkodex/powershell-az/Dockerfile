FROM mcr.microsoft.com/powershell:6.2.0-alpine-3.8

RUN pwsh -c "Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted; Install-Module -Name Az -RequiredVersion 2.2.0 -AllowClobber -SkipPublisherCheck"
