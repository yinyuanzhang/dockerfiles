FROM microsoft/dotnet:2.1-runtime AS base
WORKDIR /app

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY SnptabImportServiceCore/SnptabImportServiceCore.csproj SnptabImportServiceCore/
RUN dotnet restore SnptabImportServiceCore/SnptabImportServiceCore.csproj
COPY . .
WORKDIR /src/SnptabImportServiceCore
RUN dotnet build SnptabImportServiceCore.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish SnptabImportServiceCore.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .

VOLUME /app/SnpTabCache
VOLUME /app/Genomes
VOLUME /app/Test

ENV ASPNETCORE_ENVIRONMENT=Production

ENTRYPOINT ["dotnet", "SnptabImportServiceCore.dll"]
