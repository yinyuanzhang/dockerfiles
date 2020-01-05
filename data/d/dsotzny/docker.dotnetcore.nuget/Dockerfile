FROM microsoft/dotnet:3.0-sdk
LABEL maintainer="danny@sotzny.de"

RUN apt-get update && apt-get install -y \
     nuget \
     && rm -rf /var/lib/apt/lists/*
    