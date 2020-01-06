FROM mcr.microsoft.com/dotnet/core/sdk AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY ./web/*.csproj web/
RUN dotnet restore ./web/

# Copy everything else and build
COPY ./web ./web
WORKDIR /app/web
RUN dotnet publish -c Release -o out 

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet
WORKDIR /app
COPY --from=build-env /app/web/out .
ENTRYPOINT ["dotnet", "mor.servicequeue.dll"]