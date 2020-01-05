FROM mcr.microsoft.com/dotnet/core/sdk:3.0 AS build
WORKDIR /src

COPY src/*.csproj ./
RUN dotnet restore

COPY src/. ./
RUN dotnet publish -c Release -o out


FROM mcr.microsoft.com/dotnet/core/aspnet:3.0 AS run
WORKDIR /app

COPY --from=build /src/out ./

EXPOSE 80
ENTRYPOINT ["./TalkDirty2Me"]
