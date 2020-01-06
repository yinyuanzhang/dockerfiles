FROM microsoft/dotnet:2.1-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /src
COPY ["/Account/Aiursoft.Account.csproj", "Account/"]
COPY ["/Pylon/Aiursoft.Pylon.csproj", "Pylon/"]
RUN dotnet restore "Account/Aiursoft.Account.csproj"
COPY . .
WORKDIR "/src/Account"
RUN dotnet build "Aiursoft.Account.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "Aiursoft.Account.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "Aiursoft.Account.dll"]