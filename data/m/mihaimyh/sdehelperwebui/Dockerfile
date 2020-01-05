#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
RUN apt-get update
RUN apt-get -y install curl
COPY ["src/SdeHelper.Web.ServerHosted/SdeHelper.Web.ServerHosted.csproj", "src/SdeHelper.Web.ServerHosted/"]
COPY ["src/SdeHelper.Web.UI/SdeHelper.Web.UI.csproj", "src/SdeHelper.Web.UI/"]
COPY ["src/SdeHelper.Library.Main/SdeHelper.Library.Main.csproj", "src/SdeHelper.Library.Main/"]
RUN dotnet restore "src/SdeHelper.Web.ServerHosted/SdeHelper.Web.ServerHosted.csproj"
COPY . .
WORKDIR "/src/src/SdeHelper.Web.ServerHosted"
RUN dotnet build "SdeHelper.Web.ServerHosted.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "SdeHelper.Web.ServerHosted.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "SdeHelper.Web.ServerHosted.dll"]