FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /mine

# copy csproj and restore as distinct layers
COPY *.csproj ./
RUN dotnet restore

# copy and build everything else
COPY . ./
RUN dotnet publish -c Release -o /out

FROM microsoft/dotnet:2.2-runtime-alpine
WORKDIR /app
COPY --from=build-env /out ./
VOLUME /out
ENTRYPOINT ["dotnet", "/app/VSCodeTest.dll"]