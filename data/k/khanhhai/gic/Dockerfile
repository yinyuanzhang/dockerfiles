FROM microsoft/dotnet:2.2-aspnetcore-runtime AS base
WORKDIR /app
EXPOSE 80

FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /src
COPY ["GicInternal/GicInternal.csproj", "GicInternal/"]
RUN dotnet restore "GicInternal/GicInternal.csproj"
COPY . .
WORKDIR "/src/GicInternal"
RUN dotnet build "GicInternal.csproj" -c Release -o /app

FROM build AS publish
RUN dotnet publish "GicInternal.csproj" -c Release -o /app

FROM base AS final
WORKDIR /app
COPY --from=publish /app .
ENTRYPOINT ["dotnet", "GicInternal.dll"]