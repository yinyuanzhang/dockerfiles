#Depending on the operating system of the host machines(s) that will build or run the containers, the image specified in the FROM statement may need to be changed.
#For more information, please see https://aka.ms/containercompat

FROM mcr.microsoft.com/dotnet/core/aspnet:2.2 AS base
WORKDIR /app
EXPOSE 5000
ENV ASPNETCORE_URLS=http://*:5000

FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build
WORKDIR /src
COPY ["Portfolio.API/Portfolio.API.csproj", "Portfolio.API/"]
RUN dotnet restore "Portfolio.API/Portfolio.API.csproj"

COPY . .
WORKDIR /src/Portfolio.API
RUN dotnet build "Portfolio.API.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Portfolio.API.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
CMD dotnet Portfolio.API.dll
