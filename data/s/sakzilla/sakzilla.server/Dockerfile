FROM microsoft/aspnetcore-build:2.0 AS build-env
WORKDIR /app

# Copy everything and build
COPY ./ ./
RUN dotnet publish --configuration Release --output ../../dist/ ./src/Sakzilla.Server/Sakzilla.Server.csproj

# Build runtime image
FROM microsoft/aspnetcore:2.0
EXPOSE 5000
WORKDIR /app
COPY --from=build-env /app/dist/ ./

ENTRYPOINT ["dotnet", "Sakzilla.Server.dll"]
