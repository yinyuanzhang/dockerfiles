FROM timescale/timescaledb AS my_timescale

ENV PGDATA=/var/lib/postgresql/data/timescaledb
VOLUME /var/lib/postgresql
EXPOSE 5432

ADD install_timescaledb.sh /docker-entrypoint-initdb.d/init-user-db.sh


FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY SmartBin/SmartBin.csproj SmartBin/
RUN dotnet restore SmartBin/SmartBin.csproj
COPY . .
WORKDIR /src/SmartBin
RUN dotnet build SmartBin.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish SmartBin.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "SmartBin.dll"]
