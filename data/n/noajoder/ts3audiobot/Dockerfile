ARG REPO=mcr.microsoft.com/dotnet/core/runtime-deps
FROM $REPO:3.0-buster-slim
MAINTAINER CookieCr2nk
LABEL description="TS3Audiobot Dockerized"
#Install requires
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg curl wget unzip libopus-dev python && \
    rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

# Install .NET Core
ENV DOTNET_VERSION 3.0.1

RUN curl -SL --output dotnet.tar.gz https://dotnetcli.azureedge.net/dotnet/Runtime/$DOTNET_VERSION/dotnet-runtime-$DOTNET_VERSION-linux-x64.tar.gz \
    && dotnet_sha512='d84192fd20ff09e6bc00eca37c6e5d2c5025c7a0fd93644a1dc4e4f0fc7322689dd8ee7b331352c568b999a7ebcd909c0893abf455da354b23119334378615ca' \
    && echo "$dotnet_sha512 dotnet.tar.gz" | sha512sum -c - \
    && mkdir -p /usr/share/dotnet \
    && tar -zxf dotnet.tar.gz -C /usr/share/dotnet \
    && rm dotnet.tar.gz \
    && ln -s /usr/share/dotnet/dotnet /usr/bin/dotnet

#YT-DL Herunterladen
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl && chmod a+rx /usr/local/bin/youtube-dl

# TS3Audiobot installieren
WORKDIR /app
RUN wget -O TS3AudioBot.zip https://splamy.de/api/nightly/ts3ab/develop_dotnet_core_3_0_preview/download && unzip TS3AudioBot.zip && rm -f TS3AudioBot.zip
VOLUME /app
#Portfreigabe
EXPOSE 58913

#TS3Audiobot starten
 CMD ["dotnet", "TS3AudioBot.dll", "--non-interactive"]
