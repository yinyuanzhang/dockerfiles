FROM mcr.microsoft.com/dotnet/core/runtime:2.2-stretch-slim AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src/ServerManager
COPY . .
RUN dotnet restore
RUN dotnet build "ServerManager.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "ServerManager.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "ServerManager.dll"]