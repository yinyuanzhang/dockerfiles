FROM ubuntu:15.04

ENV DOCKER_CONTAINER=1 \
    DEBIAN_FRONTEND=noninteractive

RUN apt-key adv \
        --keyserver hkp://keyserver.ubuntu.com:80 \
        --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian wheezy main" \
        > /etc/apt/sources.list.d/mono-xamarin.list

RUN apt-get update \
    && apt-get install -yq mono-complete fsharp \
    git \
    curl \
    wget \
    && apt-get clean

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -

RUN apt-get update \
    && apt-get install -yq nodejs

RUN mozroots --import --sync \
    && yes | certmgr -ssl https://go.microsoft.com \
    && yes | certmgr -ssl https://nugetgallery.blob.core.windows.net \
    && yes | certmgr -ssl https://nuget.org

RUN ln -s /usr/lib/mono /usr/local/lib/mono


RUN npm install -g less bower
