FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["/API/Aiursoft.API.csproj", "API/"]
COPY ["/Pylon/Aiursoft.Pylon.csproj", "Pylon/"]
RUN dotnet restore "API/Aiursoft.API.csproj"
COPY . .
WORKDIR "/src/API"
RUN dotnet build "Aiursoft.API.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Aiursoft.API.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Aiursoft.API.dll"]