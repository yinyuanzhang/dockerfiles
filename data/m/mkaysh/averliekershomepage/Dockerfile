# build backend
FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY server/Server/Server.csproj Server/Server.csproj
RUN dotnet restore Server/Server.csproj
COPY server .
WORKDIR /src/Server
RUN dotnet build Server.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish Server.csproj -c Release -o /app

# build frontend
FROM node:alpine AS yarninstall
RUN apk add python2
RUN apk add build-base
RUN apk add yarn
RUN yarn global add @angular/cli
WORKDIR /src
COPY client/package.json ./package.json
COPY client/yarn.lock ./yarn.lock
RUN yarn --pure-lockfile

FROM yarninstall AS copy_client_sources
WORKDIR /src
COPY client .

FROM copy_client_sources AS ngbuild
WORKDIR /src
RUN yarn run build:production

# finalize
FROM base AS final
RUN apt-get update && apt-get install -y libgdiplus && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY --from=publish /app .
COPY --from=ngbuild /src/dist/ wwwroot/
ENTRYPOINT ["dotnet", "Server.dll"]
