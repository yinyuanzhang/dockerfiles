# 1. Prepare server side build image
FROM microsoft/dotnet:2.1-sdk as build-env
RUN curl -sL https://deb.nodesource.com/setup_12.x > setup.sh
RUN sh setup.sh 
RUN apt-get install -y nodejs
RUN node -v
WORKDIR /app
COPY PortfolioReact/*.csproj ./PortfolioReact/
RUN ls
COPY *.sln ./
RUN ls
RUN dotnet restore Portfolio.sln
 
#2 Build client-side artifacts
FROM node:8.9.4 as clientBuild
WORKDIR /ClientApp
COPY PortfolioReact/ClientApp/ .
RUN npm install
RUN npm run build
 
#3 Publish final output by merging server-side and client-side artifacts
FROM build-env as publish
COPY . ./
RUN dotnet publish -c Release -o out
#COPY --from=clientBuild ./ClientApp/build ./PortfolioReact/out/ClientApp/build
 
# Build runtime image
FROM microsoft/dotnet:2.1-aspnetcore-runtime
WORKDIR /app
COPY --from=publish /app/PortfolioReact/out/ .
EXPOSE 80
EXPOSE 443
ENTRYPOINT ["dotnet", "PortfolioReact.dll"]