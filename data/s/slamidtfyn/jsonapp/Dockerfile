FROM microsoft/dotnet:2.2-runtime-alpine AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.2-sdk-alpine AS build
WORKDIR /src
COPY dockerapp.csproj ./
RUN dotnet restore dockerapp.csproj
COPY . .
WORKDIR /src/
RUN dotnet build dockerapp.csproj -c Release -o /app -r alpine-x64

FROM build AS publish
RUN dotnet publish dockerapp.csproj -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "dockerapp.dll"]