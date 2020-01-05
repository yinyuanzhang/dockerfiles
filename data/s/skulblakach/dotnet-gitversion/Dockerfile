FROM microsoft/dotnet:2.1-sdk
LABEL maintainer="Skulblaka <skulblaka@mailbox.org>"

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \
  && apt-get update \
  && apt-get install -y apt-transport-https dirmngr unzip libgit2-24 \
  && echo "deb https://download.mono-project.com/repo/debian stable-stretch main" > /etc/apt/sources.list.d/mono-official-stable.list \
  && apt-get update \
  && apt-get install -y mono-complete \
  && rm -rf /var/lib/apt/lists/* /tmp/*

RUN export GitVersion=$(curl --silent "https://api.github.com/repos/gittools/gitversion/releases/latest" | grep -Po '"tag_name": "\K.*?(?=")' | cut -c 2-) \
  && curl -L -o GitVersion.zip "https://github.com/GitTools/GitVersion/releases/download/v$GitVersion/GitVersion_$GitVersion.zip" \
  && unzip GitVersion.zip -d /usr/bin/ \
  && rm GitVersion.zip \
  && printf '<configuration><dllmap os="linux" cpu="x86-64" wordsize="64" dll="git2-baa87df" target="/usr/lib/x86_64-linux-gnu/libgit2.so.24" /></configuration>' > \
  /usr/bin/LibGit2Sharp.dll.config \
  && printf '#!/bin/bash\nmono /usr/bin/GitVersion.exe "$@"' > /usr/bin/GitVersion && chmod +x /usr/bin/GitVersion

