FROM mono:5.8 as base

RUN apt-get update \
    && apt install curl -y \
    && curl -o /usr/local/bin/nuget.exe https://dist.nuget.org/win-x86-commandline/latest/nuget.exe \
    && alias nuget="mono /usr/local/bin/nuget.exe"
