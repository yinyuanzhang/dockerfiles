FROM jsacapdev/dotnet-cake-build:linux-0.2 AS builder

COPY ./build.cake ./
COPY ./cake-in-docker.sln ./
COPY ./src/CakeInDocker.Data/CakeInDocker.Data.csproj  ./src/CakeInDocker.Data/CakeInDocker.Data.csproj
COPY ./src/CakeInDocker.API/CakeInDocker.API.csproj  ./src/CakeInDocker.API/CakeInDocker.API.csproj
COPY ./test/CakeInDocker.API.Tests/CakeInDocker.API.Tests.csproj  ./test/CakeInDocker.API.Tests/CakeInDocker.API.Tests.csproj
RUN ./build.sh -Target=Restore

COPY ./test ./test
COPY ./src ./src

# Build, Test, and Publish
RUN ./build.sh -Target=Build && ./build.sh -Target=Test && ./build.sh -Target=PublishWeb

#App image
FROM microsoft/aspnetcore:2.0.5-stretch
WORKDIR /app
ENV ASPNETCORE_ENVIRONMENT Production
ENTRYPOINT ["dotnet", "CakeInDocker.API.dll"]
COPY --from=builder ./sln/dist .