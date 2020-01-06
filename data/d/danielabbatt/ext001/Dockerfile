FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["ext001.panoramic.systems/ext001.panoramic.systems.csproj", "ext001.panoramic.systems/"]
RUN dotnet restore "ext001.panoramic.systems/ext001.panoramic.systems.csproj"
COPY . .
WORKDIR "/src/ext001.panoramic.systems"
RUN dotnet build "ext001.panoramic.systems.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "ext001.panoramic.systems.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "ext001.panoramic.systems.dll"]