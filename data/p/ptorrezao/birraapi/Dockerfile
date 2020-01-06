FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY . ./

COPY . ./
RUN ls
RUN dotnet restore 
RUN dotnet publish -c Release -o out

# Build runtime image
FROM mcr.microsoft.com/dotnet/core/aspnet:2.2
WORKDIR /app

COPY --from=build-env /app/Birra.WebApi/out/ .

ENTRYPOINT ["dotnet", "Birra.WebApi.dll"]

