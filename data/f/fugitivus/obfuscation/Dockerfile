#obfuscation docker-container for for teaching students
#some obfuscation techniques for Windows cmd.exe and powershell.exe:
#build with docker build -f obfuscation.docker -t fugitivus/obfuscation:latest .

FROM fugitivus/ubuntu:xenial
MAINTAINER fugitivus <fugitivus@gmx.de>

#environment-variables for non-interactive shell:
#ENV DEBIAN_FRONTEND noninteractive

#install updates, some packages:
RUN apt-get update && apt-get upgrade -y\
 && apt-get install apt-utils wget apt-transport-https git -y\
 && apt-get install net-tools htop bmon joe aptitude -y\
#install powershell and download Invoke-DOSFuscation:
 && wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb\
 && dpkg -i packages-microsoft-prod.deb\
 && apt-get update && apt-get install -y powershell\
 && git clone https://github.com/danielbohannon/Invoke-Obfuscation.git\
 && git clone https://github.com/danielbohannon/Revoke-Obfuscation.git\
 && git clone https://github.com/danielbohannon/Invoke-DOSfuscation.git\
 && git clone https://github.com/danielbohannon/Invoke-CradleCrafter.git\
 && git clone https://github.com/danielbohannon/Out-FINcodedCommand.git\
#show usage each time attaching container:
 && echo "echo -e '\033[1;31m'" >> /etc/bash.bashrc\
 && echo "echo 'Run all commands inside of powershell (pwsh)'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[1;33m'" >> /etc/bash.bashrc\
 && echo "echo 'Run Invoke-Obfuscation:'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[0m'" >> /etc/bash.bashrc\
 && echo "echo 'cd Invoke-Obfuscation'" >> /etc/bash.bashrc\
 && echo "echo 'Import-Module .\Invoke-Obfuscation.psd1'" >> /etc/bash.bashrc\
 && echo "echo 'Invoke-Obfuscation\n'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[1;33m'" >> /etc/bash.bashrc\
 && echo "echo 'Run Invoke-DOSFuscation:'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[0m'" >> /etc/bash.bashrc\
 && echo "echo 'cd Invoke-DOSfuscation'" >> /etc/bash.bashrc\
 && echo "echo 'Import-Module .\Invoke-DOSfuscation.psd1'" >> /etc/bash.bashrc\
 && echo "echo 'Invoke-DOSfuscation\n'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[1;33m'" >> /etc/bash.bashrc\
 && echo "echo 'Run Revoke-DOSFuscation:'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[0m'" >> /etc/bash.bashrc\
 && echo "echo 'cd Revoke-DOSfuscation'" >> /etc/bash.bashrc\
 && echo "echo 'Import-Module .\Revoke-DOSfuscation.psd1'" >> /etc/bash.bashrc\
 && echo "echo 'Revoke-DOSfuscation\n'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[1;33m'" >> /etc/bash.bashrc\
 && echo "echo 'Run Invoke-CradleCrafter:'" >> /etc/bash.bashrc\
 && echo "echo -e -n '\033[0m'" >> /etc/bash.bashrc\
 && echo "echo 'cd Invoke-CradleCrafter'" >> /etc/bash.bashrc\
 && echo "echo 'Import-Module .\Invoke-CradleCrafter.psd1'" >> /etc/bash.bashrc\
 && echo "echo 'Invoke-CradleCrafter\n'" >> /etc/bash.bashrc\
#do some cleanup:
 && apt-get clean autoclean\
 && apt-get autoremove -y\
 && rm -rf /var/lib/{apt,dpkg,cache,log}/
