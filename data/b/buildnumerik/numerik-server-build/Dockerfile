FROM microsoft/dotnet:2.2-sdk

MAINTAINER Simon <simon@simonrichards.me>

RUN apt-get update && apt-get install -y zip curl lftp

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get update && apt-get install -y nodejs