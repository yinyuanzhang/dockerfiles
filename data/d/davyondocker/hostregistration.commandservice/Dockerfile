FROM mcr.microsoft.com/dotnet/core/runtime:2.2-stretch-slim AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["Host.Application/", "Host.Application/"]

COPY ["Host.UI.CommandService/", "Host.UI.CommandService/"]
COPY ["Host.Infrastructure.InMemoryCache/", "Host.Infrastructure.InMemoryCache/"]
COPY ["Host.Infrastructure.IntegrationEvent/", "Host.Infrastructure.IntegrationEvent/"]
COPY ["Host.Infrastructure.GregsEventStore/", "Host.Infrastructure.GregsEventStore/"]
COPY ["Host.Infrastructure.ApplicationMessaging/", "Host.Infrastructure.ApplicationMessaging/"]
COPY ["Host.Application.Extensions.Microsoft.DependencyInjection/", "Host.Application.Extensions.Microsoft.DependencyInjection/"]
COPY ["Host.Domain/", "Host.Domain/"]
COPY ["Host.Application.Infrastructure/", "Host.Application.Infrastructure/"]
COPY ["Host.Infrastructure.InMemoryEventStore/", "Host.Infrastructure.InMemoryEventStore/"]
RUN dotnet restore "Host.UI.CommandService/Host.UI.CommandService.csproj"
WORKDIR "/src/Host.UI.CommandService"
COPY ["Host.UI.CommandService/","."]
RUN dotnet build "Host.UI.CommandService.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Host.UI.CommandService.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Host.UI.CommandService.dll"]