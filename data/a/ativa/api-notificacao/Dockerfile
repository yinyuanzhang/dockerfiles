# publish
FROM microsoft/dotnet:2.1.503-sdk-alpine3.7 AS build
WORKDIR /app
COPY *.sln .
COPY src/ ./src/
COPY test/ ./test/
RUN dotnet restore\
  && dotnet publish src/Application/Application.csproj -c Release -o /app/out

# run
FROM microsoft/dotnet:2.1-aspnetcore-runtime-alpine3.7 AS runtime
WORKDIR /app
ENV ASPNETCORE_ENVIRONMENT Production
COPY --from=build /app/out ./

ENTRYPOINT ["dotnet", "Ativa.Notification.Application.dll"]
