FROM microsoft/dotnet:2.2-sdk

WORKDIR /root
RUN apt update

#
# Docker
#
RUN apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
RUN apt update
RUN apt install -y docker-ce

#
# Node10
#
RUN apt install -y curl gnupg2
RUN curl -sL https://deb.nodesource.com/setup_10.x -o nodesource_setup.sh
RUN chmod +x nodesource_setup.sh
RUN ./nodesource_setup.sh
RUN apt install -y nodejs

RUN nodejs -v
RUN npm -v

#
# Mono/GitVersion
#
RUN apt install -y git curl libcurl3 unzip mono-complete
RUN apt install -y libgit2-24
WORKDIR /tmp
RUN curl -L https://github.com/GitTools/GitVersion/releases/download/v4.0.0/GitVersion-bin-net40-v4.0.0.zip -o GitVersion.zip
RUN ls /tmp
RUN unzip GitVersion.zip -d GitVersion
RUN mv /tmp/GitVersion /opt
RUN cp /opt/GitVersion/LibGit2Sharp.dll.config /opt/GitVersion/LibGit2Sharp.dll.config.orig 
RUN echo "<configuration><dllmap os=\"linux\" cpu=\"x86-64\" wordsize=\"64\" dll=\"git2-15e1193\" target=\"/usr/lib/x86_64-linux-gnu/libgit2.so.24\" />    <dllmap os=\"osx\" cpu=\"x86,x86-64\" dll=\"git2-15e1193\" target=\"lib/osx/libgit2-15e1193.dylib\" /></configuration>" > /opt/GitVersion/LibGit2Sharp.dll.config
RUN echo '#!/bin/bash' > /usr/bin/gitversion
RUN echo 'mono /opt/GitVersion/GitVersion.exe' >> /usr/bin/gitversion
RUN chmod +x /usr/bin/gitversion

# Test Repo and GitVersion with Mono
RUN mkdir /tmp/repotest
WORKDIR /tmp/repotest
RUN git init && touch a.txt && git add -A && git commit -a -m "First commit"
RUN gitversion
RUN rm -rf /tmp/repotest

WORKDIR /app/src