FROM microsoft/dotnet:2.2-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 5001

FROM microsoft/dotnet:2.2-sdk AS build

# Setup NodeJs
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y gnupg2 && \
    wget -qO- https://deb.nodesource.com/setup_10.x | bash - && \
    apt-get install -y build-essential nodejs
# End setup

WORKDIR /src
COPY ["sn10.csproj", "./"]
RUN dotnet restore "./sn10.csproj"
COPY . .
WORKDIR /src/.
RUN dotnet build "sn10.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "sn10.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "sn10.dll"]
