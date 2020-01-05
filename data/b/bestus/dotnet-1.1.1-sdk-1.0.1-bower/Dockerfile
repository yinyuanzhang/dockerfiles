# NOTE we are currently not using this and instead are referenciing the microsoft dotnet image directly
# Keeping for reference if we need to deploy to somewhere else besides bitbucket.
FROM node:slim AS node
FROM microsoft/dotnet:aspnetcore-runtime
COPY --from=node / /
RUN npm install -g bower grunt-cli