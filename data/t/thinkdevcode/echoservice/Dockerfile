FROM microsoft/dotnet:2.2-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /src
COPY ["EchoService.csproj", "EchoService/"]
RUN dotnet restore "EchoService/EchoService.csproj"
COPY . "EchoService/"
WORKDIR "/src/EchoService"
RUN dotnet build "EchoService.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "EchoService.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "EchoService.dll"]