FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["AdsVitrina.csproj", ""]
RUN dotnet restore "./AdsVitrina.csproj"

# Setup NodeJs
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y gnupg2 && \
    wget -qO- https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y build-essential nodejs

COPY . .
WORKDIR "/src/."
RUN dotnet build "AdsVitrina.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "AdsVitrina.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "AdsVitrina.dll"]