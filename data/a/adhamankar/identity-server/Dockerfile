FROM microsoft/dotnet:2.1-sdk-alpine AS build-env
WORKDIR /app

# Copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY . ./
RUN dotnet publish -c Release -o out

# Build runtime image
FROM microsoft/dotnet:2.1-aspnetcore-runtime-alpine AS runtime
WORKDIR /app
COPY --from=build-env /app/out .

EXPOSE 80

ENTRYPOINT ["dotnet", "Identity.dll"]