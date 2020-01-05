FROM microsoft/dotnet:2.2-sdk AS build-env
WORKDIR /app

COPY Stratox.Miotiq.Billing.Billing ./Stratox.Miotiq.Billing.Billing
COPY Stratox.Miotiq.Billing.Common ./Stratox.Miotiq.Billing.Common
RUN dotnet restore Stratox.Miotiq.Billing.Billing/*.csproj
RUN dotnet publish Stratox.Miotiq.Billing.Billing/*.csproj -c Release -o out

FROM microsoft/dotnet:2.2-aspnetcore-runtime
WORKDIR /app
COPY --from=build-env /app/Stratox.Miotiq.Billing.Billing/out .
ENTRYPOINT ["dotnet", "Stratox.Miotiq.Billing.Billing.dll"]
