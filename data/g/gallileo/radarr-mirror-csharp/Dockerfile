FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY RadarrMirror.sln ./
COPY RadarrMirror/RadarrMirror.csproj ./RadarrMirror/
COPY Radarr/src/ParsingLibrary/ParsingLibrary.csproj ./Radarr/src/ParsingLibrary/
COPY yaap-dev/Yaap/Yaap.csproj ./yaap-dev/Yaap/
COPY "MySqlBackup(NetStandard)/MySqlBackup(NetStandard).csproj" "./MySqlBackup(NetStandard)/"
RUN dotnet restore

# copy and publish app and libraries
COPY ./ ./
RUN dotnet publish -c Release -o out


FROM microsoft/dotnet:2.2-runtime AS runtime
VOLUME /logs/
WORKDIR /app
COPY --from=build /app/RadarrMirror/out ./
ENTRYPOINT ["dotnet", "RadarrMirror.dll"]