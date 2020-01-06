FROM mcr.microsoft.com/dotnet/core/aspnet:3.0-buster-slim AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY ["PushService/PushService.csproj", "PushService/"]
RUN dotnet restore "PushService/PushService.csproj"
COPY . .
WORKDIR "/src/PushService"
RUN dotnet build "PushService.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "PushService.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
VOLUME ["/app/logs"]
ENTRYPOINT ["dotnet", "PushService.dll"]