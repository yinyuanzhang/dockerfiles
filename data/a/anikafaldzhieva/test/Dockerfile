FROM mcr.microsoft.com/dotnet/core/aspnet:2.2-stretch-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:2.2-stretch AS build
WORKDIR /src
COPY ["dockerapp1/dockerapp1.csproj", "dockerapp1/"]
RUN dotnet restore "dockerapp1/dockerapp1.csproj"
COPY . .
WORKDIR "/src/dockerapp1"
RUN dotnet build "dockerapp1.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "dockerapp1.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "dockerapp1.dll"]