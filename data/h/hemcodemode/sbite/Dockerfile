FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["src/Services/Services.csproj", "src/Services/"]
COPY ["src/Data/Data.csproj", "src/Data/"]
COPY ["src/Cron/Cron.csproj", "src/Cron/"]
COPY ["src/Common/Common.csproj", "src/Common/"]
COPY ["src/Core/Core.csproj", "src/Core/"]
COPY ["src/Indexer/Indexer.csproj", "src/Indexer/"]
RUN dotnet restore "src/Services/Services.csproj"
COPY . .
WORKDIR "/src/src/Services"
RUN dotnet build "Services.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Services.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Services.dll"]
