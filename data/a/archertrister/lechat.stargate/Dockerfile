FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["/Stargate/Aiursoft.Stargate.csproj", "Stargate/"]
COPY ["/Pylon/Aiursoft.Pylon.csproj", "Pylon/"]
RUN dotnet restore "Stargate/Aiursoft.Stargate.csproj"
COPY . .
WORKDIR "/src/Stargate"
RUN dotnet build "Aiursoft.Stargate.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Aiursoft.Stargate.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Aiursoft.Stargate.dll"]
