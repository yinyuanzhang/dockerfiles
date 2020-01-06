FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 53966
EXPOSE 44326

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["Docker-TestApp/Docker-TestApp.csproj", "Docker-TestApp/"]
RUN dotnet restore "Docker-TestApp/Docker-TestApp.csproj"
COPY . .
WORKDIR "/src/Docker-TestApp"
RUN dotnet build "Docker-TestApp.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Docker-TestApp.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Docker-TestApp.dll"]