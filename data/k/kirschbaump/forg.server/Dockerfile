FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY FOrg.Server/FOrg.Server.csproj FOrg.Server/
RUN dotnet restore FOrg.Server/FOrg.Server.csproj
COPY . .
WORKDIR /src/FOrg.Server
RUN dotnet build FOrg.Server.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish FOrg.Server.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "FOrg.Server.dll"]
