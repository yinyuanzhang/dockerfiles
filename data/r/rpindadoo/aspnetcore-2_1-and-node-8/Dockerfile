FROM microsoft/dotnet:2.1-aspnetcore-runtime
RUN apt-get -qq update && apt-get -qqy --no-install-recommends install \
    git \
    unzip
RUN apt-get update && apt-get install -my wget gnupg
RUN curl -sL https://deb.nodesource.com/setup_8.x |  bash -
RUN apt-get install -y nodejs
WORKDIR /app