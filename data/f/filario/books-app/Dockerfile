FROM mcr.microsoft.com/dotnet/core/aspnet:3.0 AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore

# Copy everything else and build
FROM build-env AS publish
COPY . ./
RUN dotnet publish -c Release -o out

# Build runtime image
FROM base as prod
COPY --from=publish /app/out .
RUN ls
ENTRYPOINT ["dotnet", "BooksApp.dll"]
