FROM microsoft/dotnet:2.2-aspnetcore-runtime-stretch-slim AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.2-sdk-stretch AS build
WORKDIR /src
COPY ["src/Axle.Web/Axle.Web.csproj", "src/Axle.Web/"]
COPY ["src/Axle.Infrastructure/Axle.Infrastructure.csproj", "src/Axle.Infrastructure/"]
COPY ["src/Axle.DAL/Axle.DAL.csproj", "src/Axle.DAL/"]
RUN dotnet restore "src/Axle.Web/Axle.Web.csproj"
COPY . .
WORKDIR "/src/src/Axle.Web"
RUN dotnet build "Axle.Web.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Axle.Web.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Axle.Web.dll"]
