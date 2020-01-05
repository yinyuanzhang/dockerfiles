FROM microsoft/dotnet:2.1-sdk AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY *.sln .
COPY WakeboardUK2018/*.csproj ./WakeboardUK2018/
RUN dotnet restore

# copy everything else and build app
COPY WakeboardUK2018/. ./WakeboardUK2018/
WORKDIR /app/WakeboardUK2018
RUN dotnet publish -c Release -o out


FROM microsoft/dotnet:2.1-aspnetcore-runtime AS runtime
WORKDIR /app
COPY --from=build /app/WakeboardUK2018/out ./
ENTRYPOINT ["dotnet", "WakeboardUK2018.dll"]
