FROM microsoft/dotnet:2.1-sdk
WORKDIR /app

# copy csproj and restore as distinct layers
COPY Fadzinator/*.csproj ./
RUN dotnet restore

# copy and build everything else
COPY ./Fadzinator ./

RUN dotnet publish -c Release -o out

# Build runtime image
ENTRYPOINT ["dotnet", "out/Fadzinator.dll"]