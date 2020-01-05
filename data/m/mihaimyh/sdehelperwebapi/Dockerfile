#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["src/SdeHelper.Api/SdeHelper.Api.csproj", "src/SdeHelper.Api/"]
COPY ["src/SdeHelper.Library.Main/SdeHelper.Library.Main.csproj", "src/SdeHelper.Library.Main/"]
RUN dotnet restore "src/SdeHelper.Api/SdeHelper.Api.csproj"
COPY . .
WORKDIR "/src/src/SdeHelper.Api"
RUN dotnet build "SdeHelper.Api.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SdeHelper.Api.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SdeHelper.Api.dll"]