FROM microsoft/dotnet:aspnetcore-runtime AS base
WORKDIR /app

FROM microsoft/dotnet:sdk AS build
WORKDIR /src
COPY Telegram.Bot.GLObot.Notifier.Webhook/Telegram.Bot.GLObot.Notifier.Webhook.csproj Telegram.Bot.GLObot.Notifier.Webhook/
COPY Telegram.Bot.Library/Telegram.Bot.Library.csproj Telegram.Bot.Library/
RUN dotnet restore Telegram.Bot.GLObot.Notifier.Webhook/Telegram.Bot.GLObot.Notifier.Webhook.csproj
COPY . .
WORKDIR /src/Telegram.Bot.GLObot.Notifier.Webhook
RUN dotnet build Telegram.Bot.GLObot.Notifier.Webhook.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish Telegram.Bot.GLObot.Notifier.Webhook.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Telegram.Bot.GLObot.Notifier.Webhook.dll"]
EXPOSE 8443
