FROM microsoft/dotnet:2.1-runtime AS base
WORKDIR /app

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY SnptpaeImportServiceCore/SnptpaeImportServiceCore.csproj SnptpaeImportServiceCore/
RUN dotnet restore SnptpaeImportServiceCore/SnptpaeImportServiceCore.csproj
COPY . .
WORKDIR /src/SnptpaeImportServiceCore
RUN dotnet build SnptpaeImportServiceCore.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish SnptpaeImportServiceCore.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .

VOLUME /app/SnpPaeCache
VOLUME /app/Genomes
VOLUME /app/Test

ENV ASPNETCORE_ENVIRONMENT=Production

ENTRYPOINT ["dotnet", "SnptpaeImportServiceCore.dll"]
