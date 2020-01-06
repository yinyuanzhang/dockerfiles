FROM microsoft/dotnet:2.1-sdk-alpine
LABEL maintainer="ektich@gmail.com"

RUN dotnet tool install -g Amazon.Lambda.Tools

RUN ln -s /root/.dotnet/tools/dotnet-lambda /usr/local/bin

WORKDIR /code
