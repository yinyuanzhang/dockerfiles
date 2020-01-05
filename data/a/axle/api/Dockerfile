FROM mcr.microsoft.com/dotnet/core/aspnet:3.0-buster-slim AS base
WORKDIR /app
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY ["src/Axle.Api/Axle.Api.csproj", "src/Axle.Api/"]
COPY ["src/Axle.Infrastructure/Axle.Infrastructure.csproj", "src/Axle.Infrastructure/"]
COPY ["src/Axle.DAL/Axle.DAL.csproj", "src/Axle.DAL/"]
COPY ["src/Axle.Contracts/Axle.Contracts.csproj", "src/Axle.Contracts/"]
COPY ["src/Axle.Core/Axle.Core.csproj", "src/Axle.Core/"]
RUN dotnet restore "src/Axle.Api/Axle.Api.csproj"
COPY . .
WORKDIR "/src/src/Axle.Api"
RUN dotnet build "Axle.Api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Axle.Api.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Axle.Api.dll"]