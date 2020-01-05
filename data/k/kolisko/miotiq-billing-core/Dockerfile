FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /app

COPY Stratox.Miotiq.Billing.Core ./Stratox.Miotiq.Billing.Core
COPY Stratox.Miotiq.Billing.Common ./Stratox.Miotiq.Billing.Common
RUN dotnet restore Stratox.Miotiq.Billing.Core/*.csproj
RUN dotnet publish Stratox.Miotiq.Billing.Core/*.csproj -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime
WORKDIR /app
COPY --from=build-env /app/Stratox.Miotiq.Billing.Core/out .
ENTRYPOINT ["dotnet", "Stratox.Miotiq.Billing.Core.dll"]
