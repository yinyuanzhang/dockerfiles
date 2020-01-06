## Alpine Plataform   
# FROM microsoft/dotnet:2.2-sdk-alpine AS build-env

# WORKDIR /app

# # copy and build everything else
# COPY . ./ 

# RUN set -xe \
#    && apk add --update \
#    bash \
#    git \
#    unzip \
#    gnupg \
#    nodejs\
#    nodejs-npm\
#    && rm -rf /var/cache/apk/*

# # Change work directory
# WORKDIR thrust.loreal.api

# # Install app dependencies
# RUN npm install

# # Package to output directory
# RUN dotnet publish -c Release -o out thrust.loreal.api.csproj

# # Build da imagem
# FROM microsoft/dotnet:2.2-aspnetcore-runtime-alpine

# WORKDIR /app

# # install libgdiplus
# RUN apk add libgdiplus --no-cache --repository http://dl-4.alpinelinux.org/alpine/edge/testing

# # Binds to ports
# EXPOSE  80

# COPY --from=build-env /app/thrust.loreal.api/out .
# ENTRYPOINT ["dotnet", "thrust.loreal.api.dll"]
## End Alpine

## Debian Plataform 
FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build-env

WORKDIR /app

# copy and build everything else
COPY . ./

RUN apt-get -qq update && apt-get -qqy --no-install-recommends install wget gnupg \
    bzip2 \
    git \
    unzip


# Change work directory
WORKDIR thrust.loreal.api

# Package to output directory
RUN dotnet publish -c Release -o out thrust.loreal.api.csproj

# Build da imagem
FROM mcr.microsoft.com/dotnet/core/aspnet:3.0

WORKDIR /app

# install libgdiplus
RUN apt-get update
RUN apt-get install -y libgdiplus

# Binds to ports
EXPOSE  80

COPY --from=build-env /app/thrust.loreal.api/out .

ENTRYPOINT ["dotnet", "thrust.loreal.api.dll"]
## End Debian