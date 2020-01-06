FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["oidc-dotnet-api/oidc-dotnet-api.csproj", "oidc-dotnet-api/"]
RUN dotnet restore "oidc-dotnet-api/oidc-dotnet-api.csproj"
COPY . .
WORKDIR "/src/oidc-dotnet-api"
RUN dotnet build "oidc-dotnet-api.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "oidc-dotnet-api.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "oidc-dotnet-api.dll"]