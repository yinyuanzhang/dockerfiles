FROM microsoft/dotnet:2.2-sdk AS build
WORKDIR /app

# copy csproj and restore as distinct layers
COPY *.csproj ./censo/
WORKDIR /app/censo
RUN dotnet restore

# copy and publish app and libraries
WORKDIR /app
COPY . ./censo/
WORKDIR /app/censo
RUN dotnet publish -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime AS runtime
WORKDIR /app
COPY --from=build /app/censo/out .
ENTRYPOINT ["dotnet", "Censo.dll"]