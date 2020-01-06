FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY *.sln .
COPY DockerHelloWorld/*.csproj ./DockerHelloWorld/
COPY ExcelDemo/*.csproj ./ExcelDemo/
COPY VueDemo/*.csproj ./VueDemo/
COPY AngularDemo/*.csproj ./AngularDemo/
RUN dotnet restore


# copy everything else and build app
COPY DockerHelloWorld/. ./DockerHelloWorld/
WORKDIR /app/DockerHelloWorld
RUN dotnet publish -c Release -o out


FROM microsoft/dotnet:2.2-aspnetcore-runtime AS runtime
WORKDIR /app
COPY --from=build /app/DockerHelloWorld/out ./
ENTRYPOINT ["dotnet", "DockerHelloWorld.dll"]