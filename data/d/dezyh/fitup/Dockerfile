FROM microsoft/dotnet:sdk AS build-env
WORKDIR /fitup

# Install nodejs for npm
RUN curl -sL https://deb.nodesource.com/setup_10.x |  bash -
RUN apt-get install -y nodejs

# Copy csproj and restore as distinct layers
COPY ./Source/Website/*.csproj ./
RUN dotnet restore

# Copy everything else and build
COPY ./Source/Website/ ./
RUN dotnet publish -c Release -o build

# Build runtime image
FROM microsoft/dotnet:aspnetcore-runtime

EXPOSE 5000

WORKDIR /fitup
COPY --from=build-env /fitup/build .
ENTRYPOINT ["dotnet", "Website.dll"]
