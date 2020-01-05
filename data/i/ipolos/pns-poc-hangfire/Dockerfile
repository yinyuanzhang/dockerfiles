FROM mcr.microsoft.com/dotnet/core/aspnet:2.1-stretch-slim AS base
WORKDIR /app
EXPOSE 81
EXPOSE 5001

FROM mcr.microsoft.com/dotnet/core/sdk:2.1-stretch AS build
WORKDIR /src
COPY PushNotificationsTestHangfire/PushNotificationsTestHangfire.csproj PushNotificationsTestHangfire/
RUN dotnet restore "PushNotificationsTestHangfire/PushNotificationsTestHangfire.csproj"
COPY . .
WORKDIR "/src/PushNotificationsTestHangfire"
RUN dotnet build "PushNotificationsTestHangfire.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "PushNotificationsTestHangfire.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "PushNotificationsTestHangfire.dll"]
