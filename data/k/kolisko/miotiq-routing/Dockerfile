FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /app

COPY Stratox.Miotiq.Billing.Routing ./Stratox.Miotiq.Billing.Routing
COPY Stratox.Miotiq.Billing.Common ./Stratox.Miotiq.Billing.Common
RUN dotnet restore Stratox.Miotiq.Billing.Routing/*.csproj
RUN dotnet publish Stratox.Miotiq.Billing.Routing/*.csproj -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime
WORKDIR /app
COPY --from=build-env /app/Stratox.Miotiq.Billing.Routing/out .
ENTRYPOINT ["dotnet", "Stratox.Miotiq.Billing.Routing.dll"]
