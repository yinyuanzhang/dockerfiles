FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["/OSS/Aiursoft.OSS.csproj", "OSS/"]
COPY ["/Pylon/Aiursoft.Pylon.csproj", "Pylon/"]
RUN dotnet restore "OSS/Aiursoft.OSS.csproj"
COPY . .
WORKDIR "/src/OSS"
RUN dotnet build "Aiursoft.OSS.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Aiursoft.OSS.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Aiursoft.OSS.dll"]