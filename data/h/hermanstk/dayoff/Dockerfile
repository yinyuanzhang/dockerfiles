FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env

WORKDIR /app/
COPY ./DayOffBackend/DayOffBackend.sln ./

# Copy csproj and restore as distinct layers
COPY ./DayOffBackend/DayOffBackend/DayOffBackend.csproj ./DayOffBackend/DayOffBackend.csproj
COPY ./DayOffBackend/DayOffBackend.Tests/DayOffBackend.Tests.csproj ./DayOffBackend.Tests/DayOffBackend.Tests.csproj
RUN dotnet restore

# Copy everything else and build
COPY ./DayOffBackend/DayOffBackend/ ./DayOffBackend/
COPY ./DayOffBackend/DayOffBackend.Tests/ ./DayOffBackend.Tests/
RUN dotnet publish ./DayOffBackend/DayOffBackend.csproj -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:2.2
WORKDIR /app
COPY --from=build-env /app/DayOffBackend/out .
COPY ./DayOffBackend/DayOffBackend/DayOffBackend.xml ./
ENTRYPOINT ["dotnet", "DayOffBackend.dll"]
