FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS base
RUN useradd -u 555 dockerapp\
    && mkdir /home/dockerapp\
    && mkdir /home/dockerapp/app \
    && mkdir /home/dockerapp/data \
    && mkdir /home/dockerapp/cashe \
    && chown -R dockerapp:dockerapp /home/dockerapp  \
    && addgroup dockerapp staff
WORKDIR /app
EXPOSE 8001

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
WORKDIR /src
COPY ["SnpPaeWebApi/SnpPaeWebApi.csproj", "SnpPaeWebApi/"]
COPY ["SnpPaeDAL/SnpPaeDAL.csproj", "SnpPaeDAL/"]
RUN dotnet restore "SnpPaeWebApi/SnpPaeWebApi.csproj"
COPY . .
WORKDIR "/src/SnpPaeWebApi"
RUN dotnet build "SnpPaeWebApi.csproj" -c Release --runtime ubuntu.14.04-x64 -o /app

FROM build AS publish
RUN dotnet publish "SnpPaeWebApi.csproj" -c Release --runtime ubuntu.14.04-x64 -o /app

FROM base AS final

WORKDIR /app
COPY --from=publish /app .
ENV ASPNETCORE_ENVIRONMENT=Production
ENV DOCKER_HOST_IP=172.17.0.1

RUN apt-get update && apt-get install -y --no-install-recommends net-tools iputils-ping

ENTRYPOINT ["dotnet", "SnpPaeWebApi.dll"]