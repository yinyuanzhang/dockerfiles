FROM microsoft/dotnet:2.1-sdk AS builder
WORKDIR /source
COPY . ./
RUN dotnet restore
RUN dotnet publish -c Release -o ../../output src/NuGet.Core.WebApi

# build runtime image
FROM microsoft/dotnet:2.1-aspnetcore-runtime
WORKDIR /app
COPY --from=builder /source/output .
EXPOSE 80
ENTRYPOINT ["dotnet", "NuGet.Core.WebApi.dll"]
