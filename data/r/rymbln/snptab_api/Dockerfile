FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS base
RUN useradd -u 555 dockerapp\
    && mkdir /home/dockerapp\
    && mkdir /home/dockerapp/app \
    && mkdir /home/dockerapp/data \
    && mkdir /home/dockerapp/cashe \
    && chown -R dockerapp:dockerapp /home/dockerapp  \
    && addgroup dockerapp staff
WORKDIR /app
EXPOSE 8002

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
WORKDIR /src
COPY ["SnpTabApiCore/SnpTabApiCore.csproj", "SnpTabApiCore/"]
COPY ["SnpTabDAL/SnpTabDAL.csproj", "SnpTabDAL/"]
RUN dotnet restore "SnpTabApiCore/SnpTabApiCore.csproj"
COPY . .
WORKDIR "/src/SnpTabApiCore"
RUN dotnet build "SnpTabApiCore.csproj" -c Release --runtime ubuntu.14.04-x64 -o /app

FROM build AS publish
RUN dotnet publish "SnpTabApiCore.csproj" -c Release --runtime ubuntu.14.04-x64 -o /app

FROM base AS final

WORKDIR /app
COPY --from=publish /app .
ENV ASPNETCORE_ENVIRONMENT=Production
ENV DOCKER_HOST_IP=172.17.0.1

ENTRYPOINT ["dotnet", "SnpTabApiCore.dll"]