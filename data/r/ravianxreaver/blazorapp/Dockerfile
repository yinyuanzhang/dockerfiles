FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /app

COPY *.csproj ./
RUN dotnet restore  

COPY .  ./
RUN dotnet publish -c Release -o build

FROM mcr.microsoft.com/dotnet/core/aspnet:3.0
WORKDIR /app

EXPOSE 80
COPY --from=build /app/build .
ENTRYPOINT [ "dotnet", "CICD.dll" ]