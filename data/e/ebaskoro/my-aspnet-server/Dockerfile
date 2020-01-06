#
# Dockerfile
#
#

# Use .NET Core 1.1.0 with project.json support
FROM microsoft/dotnet:1.1.0-sdk-projectjson

MAINTAINER Eki Baskoro

COPY src/Web /app
WORKDIR /app

# Build the application
RUN [ "dotnet", "restore" ]
RUN [ "dotnet", "build" ]

EXPOSE 5000/tcp

CMD [ "dotnet", "run", "--server.urls", "http://*:5000" ]
