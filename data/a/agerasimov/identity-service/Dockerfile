FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80 443
ENV ASPNETCORE_ENVIRONMENT="QA"

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY *.sln ./
COPY NuGet.Config ./
COPY MsiCoreNugetPackages ./MsiCoreNugetPackages
COPY IdentityService/IdentityService.csproj IdentityService/
RUN dotnet restore --configfile NuGet.Config
COPY . .
WORKDIR /src/IdentityService
RUN dotnet build -c Release -o /app

FROM build AS publish
RUN dotnet publish -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "IdentityService.dll"]