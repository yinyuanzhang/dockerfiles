FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["AutoProvAPI/AutoProv.API.csproj", "AutoProvAPI/"]
COPY ["AutoProvLib/AutoProv.Lib.csproj", "AutoProvLib/"]
RUN dotnet restore "AutoProvAPI/AutoProv.API.csproj"
COPY . .
WORKDIR "/src/AutoProvAPI"
RUN dotnet build "AutoProv.API.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "AutoProv.API.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "AutoProv.API.dll"]