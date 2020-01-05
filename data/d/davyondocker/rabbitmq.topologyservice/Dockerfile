FROM mcr.microsoft.com/dotnet/core/runtime:2.2-stretch-slim AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src/RabbitMQTopologyService
COPY . .
RUN dotnet restore
RUN dotnet build "RabbitMQTopologyService.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "RabbitMQTopologyService.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "RabbitMQTopologyService.dll"]