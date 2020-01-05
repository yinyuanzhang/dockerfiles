ARG NODE_IMAGE=node:8.12

FROM mcr.microsoft.com/dotnet/core/aspnet:3.0-buster-slim AS base

WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY ["PayApi/PayApi.csproj", "PayApi/"]
COPY ["Core/Core.csproj", "Core/"]
COPY ["DataAccessMongo/DataAccessMongo.csproj", "DataAccessMongo/"]
RUN dotnet restore "PayApi/PayApi.csproj"
COPY . .
WORKDIR "/src/PayApi"

FROM ${NODE_IMAGE} as node-build
WORKDIR /src
COPY PayApi/ClientApp .
RUN npm install
RUN npm run build --prod

FROM build AS publish
RUN dotnet publish "PayApi.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
COPY --from=node-build /src/dist ./ClientApp/dist

WORKDIR /app
ENTRYPOINT ["dotnet", "PayApi.dll"]