FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env
EXPOSE 5000

WORKDIR /src
COPY FeinstaubServer/FeinstaubServer.csproj ./
RUN dotnet restore
COPY FeinstaubServer/ ./
RUN dotnet publish -c Release -o ./out

FROM mcr.microsoft.com/dotnet/core/aspnet:2.2
WORKDIR /src
COPY FeinstaubServer/Entities/Addresses.csv /src/Entities/
COPY --from=build-env /src/out .
ENTRYPOINT ["dotnet", "FeinstaubServer.dll"]