FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /app

COPY Stratox.Miotiq.Billing.Fe ./Stratox.Miotiq.Billing.Fe
COPY Stratox.Miotiq.Billing.Common ./Stratox.Miotiq.Billing.Common
RUN dotnet restore Stratox.Miotiq.Billing.Fe/*.csproj
RUN dotnet publish Stratox.Miotiq.Billing.Fe/*.csproj -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime
WORKDIR /app
COPY --from=build-env /app/Stratox.Miotiq.Billing.Fe/out .
ENTRYPOINT ["dotnet", "Stratox.Miotiq.Billing.Fe.dll"]
