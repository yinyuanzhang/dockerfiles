FROM mcr.microsoft.com/dotnet/core/aspnet:2.1-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 5000

FROM mcr.microsoft.com/dotnet/core/sdk:2.1-stretch AS build
WORKDIR /src
COPY PushNotificationsTestAPI/PushNotificationsTestAPI.csproj PushNotificationsTestAPI/
RUN dotnet restore "PushNotificationsTestAPI/PushNotificationsTestAPI.csproj"
COPY . .
WORKDIR "/src/PushNotificationsTestAPI"
RUN dotnet build "PushNotificationsTestAPI.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "PushNotificationsTestAPI.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "PushNotificationsTestAPI.dll"]
