FROM mcr.microsoft.com/dotnet/core/runtime:3.0-buster-slim AS base
WORKDIR /app

FROM mcr.microsoft.com/dotnet/core/sdk:3.0-buster AS build
WORKDIR /src
COPY ["TimeWriter/TimeWriter.csproj", "TimeWriter/"]
RUN dotnet restore "TimeWriter/TimeWriter.csproj"
COPY . .
WORKDIR "/src/TimeWriter"
RUN dotnet build "TimeWriter.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "TimeWriter.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
VOLUME /app/out
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TimeWriter.dll"]