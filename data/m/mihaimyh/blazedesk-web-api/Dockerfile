FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["BlazeDesk.API/BlazeDesk.API.csproj", "BlazeDesk.API/"]
RUN dotnet restore "BlazeDesk.API/BlazeDesk.API.csproj"
COPY . .
WORKDIR /src/BlazeDesk.API
RUN dotnet build "BlazeDesk.API.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "BlazeDesk.API.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "BlazeDesk.API.dll"]