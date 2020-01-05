FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /app

COPY AudiobookLibrary.Web/*.csproj ./AudiobookLibrary.Web/
COPY AudiobookLibrary.Core/*.csproj ./AudiobookLibrary.Core/
RUN dotnet restore ./AudiobookLibrary.Web/AudiobookLibrary.Web.csproj

COPY AudiobookLibrary.Web/. ./AudiobookLibrary.Web/
COPY AudiobookLibrary.Core/. ./AudiobookLibrary.Core/
WORKDIR /app/AudiobookLibrary.Web
RUN dotnet publish -c Release -o out

#Angular build
FROM node as nodebuilder
WORKDIR /app/ClientApp
ENV PATH /app/ClientApp/node_modules/.bin:$PATH
COPY AudiobookLibrary.Web/ClientApp/package.json ./
RUN npm install
COPY AudiobookLibrary.Web/ClientApp/. ./
RUN ng build --prod

FROM mcr.microsoft.com/dotnet/core/aspnet:3.0 AS runtime
WORKDIR /app
COPY --from=build /app/AudiobookLibrary.Web/out ./
COPY --from=nodebuilder /app/wwwroot/. ./wwwroot/
ENTRYPOINT ["dotnet", "AudiobookLibrary.Web.dll"]