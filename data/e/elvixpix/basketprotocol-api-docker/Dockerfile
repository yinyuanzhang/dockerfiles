FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
WORKDIR /src
COPY ["basketprotocol-api.csproj", "./"]
RUN dotnet restore "./basketprotocol-api.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "basketprotocol-api.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "basketprotocol-api.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "basketprotocol-api.dll"]
