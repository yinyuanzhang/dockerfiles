FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["/Kahla.Server/Kahla.Server.csproj", "Kahla.Server/"]
COPY ["/Pylon/Aiursoft.Pylon.csproj", "Pylon/"]
RUN dotnet restore "Kahla.Server/Kahla.Server.csproj"
COPY . .
WORKDIR "/src/Kahla.Server"
RUN dotnet build "Kahla.Server.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Kahla.Server.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Kahla.Server.dll"]
