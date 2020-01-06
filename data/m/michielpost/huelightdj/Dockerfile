FROM mcr.microsoft.com/dotnet/core/aspnet:3.1-buster-slim AS base
WORKDIR /app
EXPOSE 59919
EXPOSE 44339
EXPOSE 80

FROM mcr.microsoft.com/dotnet/core/sdk:3.1-buster AS build
WORKDIR /src
COPY ["HueLightDJ.Web/HueLightDJ.Web.csproj", "HueLightDJ.Web/"]
COPY ["HueLightDJ.Effects/HueLightDJ.Effects.csproj", "HueLightDJ.Effects/"]
RUN dotnet restore "HueLightDJ.Web/HueLightDJ.Web.csproj"
COPY . .
WORKDIR "/src/HueLightDJ.Web"
RUN dotnet build "HueLightDJ.Web.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "HueLightDJ.Web.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "HueLightDJ.Web.dll"]
