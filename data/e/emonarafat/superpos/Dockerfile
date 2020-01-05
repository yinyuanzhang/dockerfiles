FROM microsoft/dotnet:2.2-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /src
COPY coderush/coderush.csproj coderush/
RUN dotnet restore coderush/coderush.csproj
COPY . .
WORKDIR /src/coderush
RUN dotnet build coderush.csproj -c Release -o /app

FROM build AS publish
RUN dotnet publish coderush.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "coderush.dll"]
