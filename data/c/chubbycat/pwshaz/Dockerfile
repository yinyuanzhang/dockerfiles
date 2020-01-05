FROM microsoft/powershell
WORKDIR  /var/pwshaz
ADD setup-psazure.ps1 ./
ADD pwsh4partners ./
RUN pwsh ./setup-psazure.ps1
