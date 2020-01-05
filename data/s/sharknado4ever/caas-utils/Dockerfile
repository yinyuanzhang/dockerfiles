FROM microsoft/dotnet:2.2-aspnetcore-runtime-stretch-slim AS base
WORKDIR /app
ENV ASPNETCORE_URLS=http://+:8080
EXPOSE 8080

ENV LOCALHOST_ES_PATH http://localhost:9200
ENV LOCAL_ELASTIC_PROBE http://localhost:9200

FROM microsoft/dotnet:2.2-sdk-stretch AS build
WORKDIR /src
COPY ["Caas.Utils.API/Caas.Utils.API.csproj", "Caas.Utils.API/"]
COPY ["Caas.Utils.Core/Caas.Utils.Core.csproj", "Caas.Utils.Core/"]
RUN dotnet restore "Caas.Utils.API/Caas.Utils.API.csproj"
COPY . .
WORKDIR "/src/Caas.Utils.API"
RUN dotnet build "Caas.Utils.API.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Caas.Utils.API.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Caas.Utils.API.dll"]