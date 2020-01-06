FROM mcr.microsoft.com/dotnet/core/sdk:2.2 AS build-env
WORKDIR /app

COPY . ./
RUN dotnet publish ETX.Onboarding.Api -c Release -o out

FROM mcr.microsoft.com/dotnet/core/aspnet:2.2
WORKDIR /app
COPY --from=build-env /app/ETX.Onboarding.Api/out .

ENTRYPOINT ["dotnet", "etx-onboarding-api.dll"]