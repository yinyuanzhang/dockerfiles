# STAGE - BUILD
FROM microsoft/dotnet:2.1-sdk as build
WORKDIR /app/src
COPY src/*.sln ./
COPY src/*/*.csproj ./
RUN for file in ./*.csproj ; \
    do mkdir -p "${file%.*}" && \
    mv $file "${file%.*}" ; done
RUN dotnet restore *.Service

COPY src ./
RUN dotnet publish *.Service -c Release --no-restore -o /app/artifacts/publish

# STAGE - DEPLOY
FROM microsoft/dotnet:2.1-aspnetcore-runtime as deploy
ENV ASPNETCORE_URLS=http://+
EXPOSE 80
WORKDIR /app
COPY --from=build /app/artifacts ./
WORKDIR /app/publish
CMD [ "sh", "-c", "dotnet *.Service.dll" ]
