FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["/Developer/Aiursoft.Developer.csproj", "Developer/"]
COPY ["/Pylon/Aiursoft.Pylon.csproj", "Pylon/"]
RUN dotnet restore "Developer/Aiursoft.Developer.csproj"
COPY . .
WORKDIR "/src/Developer"
RUN dotnet build "Aiursoft.Developer.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Aiursoft.Developer.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Aiursoft.Developer.dll"]